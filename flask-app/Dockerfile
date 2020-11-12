# Ejemplo de multi-stage builds que genera un artefacto que puede ser copiado en las siguientes etapas
FROM ubuntu:20.04 AS make-lib

WORKDIR /app

RUN echo FOO BAR FOO BAR > artifact



FROM python:3.9-slim

WORKDIR /usr/src/app

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
