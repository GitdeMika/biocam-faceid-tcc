# Use uma imagem base, como o Python
FROM python:3.9-slim

# Instale dependências do sistema (se necessário)
RUN apt-get update && apt-get install -y libpq-dev

# Crie e defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos para o contêiner
COPY . /app

# Instale dependências do projeto
RUN pip install -r requirements.txt

# Defina o comando de inicialização
CMD ["python", "site.py"]

