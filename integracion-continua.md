# CI/CD con Docker

La integración continua con Docker es mucho más simple que sin contenedores:

* Todos los pipelines para todas las aplicaciones van a ser iguales
* Todo lo necesario para construir la aplicación está ya definido en código, en el Dockerfile
* Se puede contruir la aplicación en local y en el servidor, exactamente igual
* Todos los entornos compartirán la misma imagen, muy sencillo promocionar código
* Todos los artefactos será imágenes de Docker, fáciles de administrar en cualquier docker registry.

Para construir cualqueir aplicación utilizaremos `docker build`. Podemos taggear la imagen con la versión del código que contiene o con el commit ID por ejemplo:

`docker build -t <NOMBRE_IMAGEN>:<VERSION/COMMIT> .`

La imagen siempre es fija (aunque puedes tener una variante con dependencias de desarrollo y otra sin ellas por ejemplo). Promocionar la imagen de entorno en entorno consiste simplemente en desplegar la imagen con la configuración correcta para dicho entorno.

Hay distintos métodos que se pueden utilizar para pasar parámetros de configuración:

1. Variables de entorno

Podemos pasar variables de entorno al ejecutar docker run con la opción `-e` 

`docker run -e NAME=VALUE -e NAME2=VALUE2 nachomillangarcia/my-flask`

O tener un archivo con todas las variables y utilizarlo con la opción `--env-file`:

`docker run -d -p 5000:5000 --name flask --env-file environments/staging/env nachomillangarcia/my-flask`

2. Montando archivos de configuración

Con la opción `-v`

`docker run -d -p 5000:5000 -v $PWD/environments/staging/config.py:/usr/src/app/config.py nachomillangarcia/my-flask`

Es la opción más completa y flexible.

3. Pasando argumentos con el CMD

El CMD se puede personalizar en cada ejecución del contendor. Todo lo que pongamos a continuación de la imagen en `docker run` sustituirá al CMD por defecto de la imagen. De esta forma podemos ejecutar un comando distinto o con argumentos distintos:

`docker run -d -p 5000:5000 nachomillangarcia/my-flask python app.py ARG1`

## Desarrollo en local con Docker

Para facilitar el desarrollo de código dentro de contenedores, se puede montar el código fuente como un volumen del contenedor:

`docker run -v src:/usr/src/app nachomillangarcia/my-flask`

De esta forma los cambios que hagamos en tiempo real en el código fuente quedarán reflejados dentro del contenedor. Depende del proceso que se esté ejecutando el leer estos cambios en tiempo real, como hace por ejemplo Flask por defecto.

## VSCode

Si desarrollas con VSCode tendrás a tu disposición la extensión para contenedores Docker, que te permite gestionar todos los contenedores desde VSCode, inspeccionar el sistema de archivos, e incluso abrir una instancia del propio VSCode en cualquiera de ellos y modificar el código fuente en tiempo real.

[https://code.visualstudio.com/docs/containers/overview](https://code.visualstudio.com/docs/containers/overview)

También puedes configurar el runtime de Python para que tus aplicaciones se ejecuten dentro de un contenedor con las mismas opciones que tendrías en tu host (breakpoints, debugging, etc). Guía paso a paso: [https://code.visualstudio.com/docs/containers/quickstart-python](https://code.visualstudio.com/docs/containers/quickstart-python)