# Imagen base de Python
FROM python:3.10

# Directorio del contenedor
WORKDIR /app

# Archivos necesarios para el contenedor
COPY requirements.txt ./
COPY webscraping.py ./

# Instalacion de dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Ejecucion del script
CMD ["python", "webscraping.py"]
