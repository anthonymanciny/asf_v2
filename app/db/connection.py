import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.Base import Base

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Obter os valores das variáveis de ambiente
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD", "")  # Senha do banco, padrão vazio
DATABASE_NAME = os.getenv("DB_NAME")
HOST = os.getenv("DB_HOST", "localhost")  # Host do banco, padrão localhost
PORT = os.getenv("DB_PORT", "3306")  # Porta do banco, padrão 3306

# Verificar se todas as variáveis foram carregadas corretamente
if not USER or not DATABASE_NAME:
    raise ValueError("Variáveis de ambiente 'DB_USER' ou 'DB_NAME' não definidas!")

# Construir a URL de conexão com o banco de dados
DB_URL = f"mariadb+mariadbconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}"

# Verificar se a URL foi formada corretamente
print("Banco de dados URL:", DB_URL)

# Criando o engine (conexão com o banco)
engine = create_engine(DB_URL, echo=True)

# Criando as tabelas no banco
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")

# Criando uma fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
