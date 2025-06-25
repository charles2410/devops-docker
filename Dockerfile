# Imagen base ligera de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto (incluye app.py)
COPY . .

# Expone el puerto que usa Flask
EXPOSE 5000

# Comando por defecto para ejecutar la app
CMD ["python", "app.py"]

