#Primero se coloca la version de python con la que se trabajara todo el proyecto
FROM python:3.8

#Se crea una carpeta (WORKDIR) donde se guardara todo el proyecto
WORKDIR /app
#Se copia el archivo en el cual se esta trabajando > la nueva carpeta en doker
COPY requirements.txt /app/requirements.txt

#Instala las dependencias --sin cache --auto actualizar -instalar
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

#Copia todo el archivo ("." = todo hacia la carpeta "app" creada)
COPY . /app

#Comando BASH para que se mantenga encendido el contenedor
CMD bash -c "while true; do sleep 1; done"