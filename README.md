# 📋 API Gerenciador de Tarefas

Uma API REST para gerenciar tarefas (to-do), construída com **FastAPI** e **SQLAlchemy**. Permite criar, listar, atualizar e apagar tarefas, com persistência em banco de dados, testes automatizados e suporte a Docker.

## 🛠️ Tecnologias

- **Python**
- **FastAPI** — framework da API
- **SQLAlchemy** — ORM para o banco de dados
- **Pydantic** — validação dos dados
- **SQLite** — banco de dados
- **pytest** — testes automatizados
- **Docker** — empacotamento da aplicação

## 🚀 Como rodar

### Localmente

```bash
# 1. Instale as dependências
pip install -r requirements.txt

# 2. Suba a API
uvicorn main:app --reload
```

A API ficará disponível em `http://localhost:8000`.
A documentação interativa fica em `http://localhost:8000/docs`.

### Com Docker

```bash
# Constrói a imagem
docker build -t gerenciador-tarefas .

# Roda o container
docker run -p 8000:8000 gerenciador-tarefas
```

## 🧪 Testes

```bash
pytest
```

## 📡 Endpoints

| Método | Endpoint | Descrição |
|--------|----------------|-----------------------------------|
| GET | `/` | Mensagem de boas-vindas |
| POST | `/tarefas` | Cria uma tarefa nova |
| GET | `/tarefas` | Lista todas as tarefas |
| GET | `/tarefas/{id}` | Busca uma tarefa pelo id |
| PUT | `/tarefas/{id}` | Atualiza uma tarefa |
| DELETE | `/tarefas/{id}` | Apaga uma tarefa |

### Exemplo de corpo (criar tarefa)

```json
{
  "titulo": "Estudar para o estágio",
  "descricao": "Revisar FastAPI e SQL"
}
```

## 📁 Estrutura do projeto

```
gerenciador-tarefas/
├── main.py            # Aplicação FastAPI e endpoints
├── models.py          # Modelo SQLAlchemy (tabela)
├── schemas.py         # Schemas Pydantic (validação)
├── database.py        # Conexão e sessão do banco
├── test_main.py       # Testes automatizados
├── requirements.txt   # Dependências
├── Dockerfile         # Empacotamento Docker
└── README.md
```
