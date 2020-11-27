# Serverless

Aunque no utilice contenedores necesariamente, serverless es un modelo de arquitectura y despliegue que cumple muchas de las ventajas que buscamos cuando utilziamos contenedores.

Se pueden distinguir dos tipos:

1. Containers as a service: Se refiere a la ejecución de contenedores como servicio. Es decir, nosotros le damos la imagen de Docker (y ciertos parámetros) y el servicio la ejecuta sin que nos preocupemos por la infraestructura. Puede ejcutarla con autoescalado o directamente bajo demanda como respuesta a eventos.

Este es el tipo que tenemos con AWS ECS con Fargate.

2. Functions as a service: En este caso le damos una función programadas según los parámetros que pida el servicio, y este la ejecuta automáticamente bajo demanda como respuesta a eventos.

Esto es lo que tenemos en AWS Lambda


Las principales característica de un servicio serveless son:

* La abstracción de toda la infraestructura necesaria (hosts, networking, etc)
* Escalado proporcional al uso. Puede ser con autoescalado o directamente con ejecuciones por cada petición. Se suele seguir la norma uso 0 = gasto 0.


### AWS Lamda
<img src="img/aws-lambda-logo.svg" alt="lambda" width="250px">

Es el servicio de FaaS de AWS, que puede ejecutar la función que queramos como respuesta a varias fuentes de eventos como peticiones HTTP, sistemas de colas, cambios en buckets de S3 etc. Muy útiles sobre todo para automatizar tareas asíncronas.

En Lambda crearemos una función del tipo

```
import json

def lambda_handler(event, context):
    name = event["name"]
    return {
        'statusCode': 200,
        'body': name
    }

```

Que recibe información del evento que la ha disparado, ejecuta su función y termina con unos datos que devolverá al evento (una respuesta HTTP por ejemplo).


Para desplegar este tipo de funciones, con todos los parámetros como código y fácil de automatizar, podemos utilizar el Serverless Framework: [https://www.serverless.com/](https://www.serverless.com/)