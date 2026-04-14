<h1 align="center" style="font-weight: bold;">Cashback System</h1>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/css-%23663399.svg?style=for-the-badge&logo=css&logoColor=white)
[![PRs Welcome](https://camo.githubusercontent.com/9f7e5545529be47a15e7ce5a8c995e9ff221d14e9f9d194bfc9e3b0e127f30e0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5052732d77656c636f6d652d677265656e3f7374796c653d666f722d7468652d6261646765)](http://makeapullrequest.com)

<p align="center">
  <b>Eu fiz esse projeto a partir de um desafio para vaga de estágio da Nology. Nele criei um sistema de cashback para uma suposta fintech, baseado em regras de valor e tipo de cliente. Com um bônus maior para clientes VIP, e dobro de cashback para compras acima de R$ 500.</b>
</p>

## Sumário
  
- [Instalação](#instalacao)
- [Aplicação](#aplicacao)
- [O que eu aprendi neste projeto](#aprendi)
- [Contribuição](#contribuicao)
  
</details>

<h2 id="instalacao">Instalação</h2>

<h3>Instalando Python</h3>

Tenha certeza de ter o Python instalado no seu sistema. Visite https://www.python.org/downloads para acessar.

<h3>Instalando PostgreSQL</h3>

1. Tenha certeza de ter o PostgreSQL instalado no seu sistema. Visite https://www.python.org/downloads para acessar.

2. Durante a instalação, crie uma senha que você lembre para acessar a base de dados e utiliza-la no código.

3. Mantenha a porta padrão como `5432`

4. Abra o `pgAdmin 4` no menu Iniciar.

5. No pgAdmin, clique com o botão direito em `Servers > PostgreSQL > Databases`.

6. Selecione `Create > Database` e dê o nome de `cashback_db`.

<h3>Instruções para Local</h3>

1. Clone o repositório git:

```bash
$ git clone https://github.com/NovaLosf/cashback-system.git
```

2. Navegue para o repositório clonado:

```bahs
$ cd cashback-system
```

3. Crie um ambiente virtual:

```bahs
$ python -m venv venv
```

4. Faça a instalação do `requirements.txt`:

```bahs
$ python -m pip install -r requirements.txt
```

5. Atualize as credenciais de sua base de dados no `database.py`.

<h2 id="aplicacao">Aplicação</h2>

Esse sistema de cashback funciona para execução local, através da sua base de dados via PostgreSQL.

Para executar:

1. Rode o servidor no terminal:

```bahs
$ uvicorn main:app --reload
```

2. Abra o arquivo `index.html`.

<h2 id="aprendi">🧠 O que eu aprendi neste projeto</h2>

- Criação de **API** com **FastAPI**.
- Integração com banco de dados **PostgreSQL**.
- Programação FrontEnd com **HTML, CSS e JavaScript**.

<h2 id="contribuicao">⭐ Contribuição</h2>

**Se estiverem interessados em sugerir novas ideias, ou sugestões sintam-se livres para contribuir!**

```bash
git clone https://github.com/NovaLosf/cashback-system.git
```

```bash
git checkout -b feature/NAME
```

1. Siga os padrões de commit.

2. Abra uma solicitação de pull explicando o problema resolvido ou o recurso criado!