from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Conexão com o banco (SQLite = só um arquivo, fácil de rodar em qualquer lugar)
SQLALCHEMY_DATABASE_URL = "sqlite:///./tarefas.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},  # necessário para SQLite + FastAPI
)

# A fábrica de sessões (cada requisição abre a sua)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# A classe-pai de todos os modelos
Base = declarative_base()


# Entrega uma sessão para o endpoint e a fecha no final
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
