# Ejemplo de multi-stage builds que genera un artefacto que puede ser copiado en las siguientes etapas
FROM ubuntu:20.04 AS make-lib

WORKDIR /app

RUN echo FOO BAR FOO BAR > artifact


FROM python:3.9-slim

# Argumentos para pasar durante docker build
ARG API_KEY

# Carpeta "home" de la imagen
WORKDIR /usr/src/app

# Labels con cualquier metadata
LABEL maintainer="nachomillangarcia@gmail.com"

# Variables de entorno
ENV FOO=BAR

# Puertos que expone la imagen
EXPOSE 5000

# Instalación de librerias con apt
RUN apt update && \
    apt --no-install-recommends install -y \
      ffmpeg \
      python3-dev && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get purge --auto-remove && \
    apt-get clean

# Descargar e instalar dependencias
ADD https://github.com/wagoodman/dive/releases/download/v0.9.2/dive_0.9.2_linux_amd64.deb dive.deb

RUN dpkg -i dive.deb

# Imprimir un build arg
RUN echo ${API_KEY}

# Copiar artefactos de etapas anteriores 
COPY --from=make-lib /app/artifact artifact

# Instalar dependencias con pip
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Copiar el docker entrypoint
COPY docker-entrypoint.sh /docker-entrypoint.sh

# Copiar el código fuente
COPY src .

# Comando inicial que ejecutará el contenedor
ENTRYPOINT [ "/docker-entrypoint.sh" ]

CMD [ "python", "app.py" ]
