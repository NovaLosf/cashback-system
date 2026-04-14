"""
Cashback API
API to calculate cashback
Author: Lucas Faria
Date: April 2026
"""

from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
import database

# Dependency to provide a database session to each request
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(title="Cashback API")

# CORS Middleware configuration to allow Cross-Origin requests from the Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_CASHBACK_RATE = 0.05       # 5% base rate
VIP_BONUS_RATE = 0.10           # 10% extra for VIPs
PROMOTION_THRESHOLD = 500.0     # Value required to trigger multiplier
PROMOTION_MULTIPLIER = 2        # Multiplies the rate if threshold is met

# Data model for incoming calculation requests
class CashbackRequest(BaseModel):
    purchase_value: float
    is_vip: bool

@app.post("/calculate")
async def calculate_cashback_endpoint(data: CashbackRequest, request: Request, db: Session = Depends(get_db)):
    """
    Calculates the cashback, saves the transaction to
    the database, and returns the detailed result to the user.
    """
    user_ip = request.client.host

    # Defines the applicable rates
    current_rate = BASE_CASHBACK_RATE
    if data.purchase_value > PROMOTION_THRESHOLD:
        current_rate *= PROMOTION_MULTIPLIER

    # Calculate base cashback and apply VIP bonus
    cashback = data.purchase_value * current_rate
    if data.is_vip:
        cashback += (cashback * VIP_BONUS_RATE)

    # Create a new database record using the ORM model
    new_record = database.CashbackHistory(
        user_ip=user_ip,
        purchase_value=data.purchase_value,
        customer_type="VIP" if data.is_vip else "Normal",
        cashback_amount=round(cashback, 2)
    )

    # Persist data to PostgreSQL
    db.add(new_record)
    db.commit()

    # Return JSON response aligned with Frontend expectations
    return {
        "client_ip": user_ip,
        "purchase_value": data.purchase_value,
        "customer_type": "VIP" if data.is_vip else "Normal",
        "cashback": round(cashback, 2)
    }

@app.get("/history")
async def get_history_endpoint(request: Request, db: Session = Depends(get_db)):
    """
    Queries the database for all records matching the requester's IP address.
    """
    user_ip = request.client.host

    # Fetching records from the 'cashback_history' table filtered by IP
    history_records = db.query(database.CashbackHistory).filter(
        database.CashbackHistory.user_ip == user_ip
    ).all()

    return history_records