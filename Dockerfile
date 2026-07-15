FROM python:3.12

WORKDIR /app

# Instala as dependências primeiro (aproveita o cache do Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Comando que sobe a API quando o container inicia
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
