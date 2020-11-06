# Docker Compose

Docker compose es una herramienta que permite levantar contenedores definiendo todos sus parámetros en un fichero `docker-compose.yml`.

Es equivalente a `docker run`, pero definiendo todas las características de los contenedores en fichero en lugar de como parámetros de `docker run`. También permite gestionar redes y volúmenes, entre otras características.

Introducción a docker-compose: [https://docs.docker.com/compose/](https://docs.docker.com/compose/)

Instalación de docker-compose (En Mac y Windows no es necesario): [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

Referencia para crear el archivo `docker-compose.yml`: [https://docs.docker.com/compose/compose-file/](https://docs.docker.com/compose/compose-file/)

Ver la aplicación flask-app para un ejemplo.

Todos los comandos a continuación se deben ejecutar desde el mismo directorio donde haya un archivo `docker-compose.yml`

#### Para levantar los contenedores

`docker-compose up -d`

#### Para construir las imágenes

`docker-compose build`

#### Para subir las imágenes

`docker-compose push`


#### Para destruir los contenedores

`docker-compose stop`
`docker-compose rm`