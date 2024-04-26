# Imagen oficial de Python como imagen base
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /code

# Copiar los archivos de requisitos e instalar las dependencias
COPY ./requirements.txt /code/
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copiar el resto del código de la aplicación
COPY ./app /code/app

# Comando para ejecutar la aplicación usando uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
