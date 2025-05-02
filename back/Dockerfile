FROM python:3.12

# Define diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos da API
COPY . .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão (roda a API)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

RUN pip install --no-cache-dir -r requirements.txt

