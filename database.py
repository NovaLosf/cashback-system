"""
Cashback Database
Connect the app to the database
Author: Lucas Faria
Date: April 2026
"""

import os
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DB_USER = "postgres"
DB_PASS = "Desafio"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "cashback_db"

"""
This will try to get the 'DATABASE_URL' from the cloud environment.
If it doesn't find it, it uses your local PostgreSQL.
"""
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# The "home base" for the actual database connection.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create actual database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all ORM models to inherit from
Base = declarative_base()

class CashbackHistory(Base):
    """
    Represents the 'cashback_history' table in the database.
    Stores every calculation made, linked to the user's IP for tracking.
    """
    __tablename__ = "cashback_history"

    id = Column(Integer, primary_key=True, index=True)
    user_ip = Column(String)                                    # Origin IP address of the request
    purchase_value = Column(Float)                              # Original transaction amount
    customer_type = Column(String)                              # Categorization: "VIP" or "Normal"
    cashback_amount = Column(Float)                             # The calculated cashback value saved
    created_at = Column(DateTime, default=datetime.utcnow)      # Timestamp of the transaction

# Create all tables defined in the Base metadata
Base.metadata.create_all(bind=engine)