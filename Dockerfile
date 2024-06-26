FROM python:3.9-slim

# Instalar dependencias de sistema necesarias para mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    libmariadb-dev \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /code

# Copiar solo el archivo requirements.txt inicialmente
COPY ./requirements.txt /code/

# Instalar dependencias de Python
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copiar el resto del código de la aplicación
COPY ./app /code/app

# Comando para ejecutar la aplicación usando Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
