# ECS

<img src="img/ecs.png" alt="ecs" width="250px">

ECS (Elastic Container Services) es un orquestador de contenedores propio de AWS. Un orquestador nos permite ejecutar contenedores en un clúster de nodos. él se encarga de conocer el estado de cada nodo y levantar los contenedores en ellos, mientras nosotros tratamos todo el clúster como una caja negra. 

Esto nos permite despelgar aplicaciones en alta disponibildad, con réplicas repartidas en distintos hosts en distintas regiones o zonas de disponibilidad. Mientras mantenemos la simplicidad gracias a que todas las cargas de trabajo se despliegan de la misma forma (contenedores), y utilizamos los orquestadores para que los levanten automáticamente. 

Los orquestadores son el siguiente nivel de abstracción: con contenedores podíamos levantar cualquier carga de trabajo en cualquier host. Con los orquestadores podemos desplegar contenedores en clústers de hosts.

### Guías y tutoriales para comenzar con ECS

Los oficiales de AWS son buenos, cortos y muestran una característica distinta en cada uno:

[https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-tutorials.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-tutorials.html)

Otros buenos para comanzar desde cero y tener resultados rápidamente:

[https://medium.com/boltops/gentle-introduction-to-how-aws-ecs-works-with-example-tutorial-cea3d27ce63d](https://medium.com/boltops/gentle-introduction-to-how-aws-ecs-works-with-example-tutorial-cea3d27ce63d)

[https://www.freecodecamp.org/news/amazon-ecs-terms-and-architecture-807d8c4960fd/](https://www.freecodecamp.org/news/amazon-ecs-terms-and-architecture-807d8c4960fd/)

### Objetos básicos de ECS

#### Task

Una task en ECS es simplemente un contenedor ejecutándose en un cluster de ECS. Una task en realidad puede tener varios contenedores que se ejecutan conjuntamente (es decir, que tiene que ser levantados en un mismo host, por ejemplo un Nginx y una aplicación Python, siempre deberían ir juntos).

#### Task definition

Una task definition es simplemente una plantilla a partir de la cual se crean tasks. Contiene todos los parámetros necesarios para levantar esos contenedores correctamente. Las tasks definition no están asociadas a ningú clúster sino que pueden valer para cualquiera de ellos.

[https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html)

Referencia: [https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html)

#### Revision

Revision es una versión de una task defintion. En realidad cuando desplegamos task definition estamos desplegando una revision en concreto. Si no se especifica ninguna revision concreta, se utiliza la más reciente.

#### Service
Un service representa una aplicación desplegada en ECS. Se compone de una o varias replicas (tasks) todas iguales entre sí (de la misma task definition). Además puede añadir un balanceador de carga para gestionar el tráfico hacia todas las réplicas.

El service simplemente se ocupa de que siempre haya el número de réplicas especificado, creando o destruyendo tasks, incluyendo en los despliegues de nuevas versiones.

[https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html)

Referencia: [https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service_definition_parameters.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service_definition_parameters.html)

#### Cluster
Un cluster de ECS engloba los hosts que van a ejecutar los contenedores (más adelante hablamos de ello), las task que se levantarán en esas instancias, y los services que controlan esas task. Todos estos objetos pertenecen necesariamente a un clúster en concreto.


### Tipos de cluster

#### AWS Fargate 

Al crear un clúster puedes especificar que sea de tipo AWS Fargate. Fargate es un servicio de AWS que permite levantar contenedores sin tener que preocuparnos por las máquinas virtuales que los ejecutan. AWS las gestiona por nosotros. No es necesario configurar nada de AWS Fargate, simplemente crear un clúster de este tipo. 

Fargate factura por CPU y memoria reservada para cada contenedor. Es un modelo que escala con el uso y uso 0 implica gasto 0.

[https://aws.amazon.com/fargate/](https://aws.amazon.com/fargate/)

#### EC2 Linux

Por contra, en este tipo de clúster de ECS sí que gestionamos nosotros las máquinas de EC2 que ejecutarán nuestros contenedores. ECS nos da facilidades para hacerlo como una AMI con todo el software instalado por defecto, reglas de autoescalado, etc. Este modo da mayor flexibilidad, al poder elegir nosotros el tipo de máquina, poder personalizar el software etc. Pero siempre será más complejo de gestionar que simplemente levantar los contenedores con Fargate.

En este modo, se factura por las máquinas virtuales que tenemos levantadas (estén o no ejecutando contenedores).

[https://docs.aws.amazon.com/AmazonECS/latest/developerguide/application_architecture.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/application_architecture.html)


### Herramientas de ECS

Podemos interactuar con ECS de 3 modos distintos:

#### Consola web

Podemos realizar todas las acciones a través de la consola web (crear cualquier objeto, desplegarlos, etc.)

[https://console.aws.amazon.com/ecs/home?region=us-east-1#/getStarted](https://console.aws.amazon.com/ecs/home?region=us-east-1#/getStarted)

#### AWS CLI

Igualmente con el AWS CLI podemos realizar todas las acciones, con la ventaja de que podemos definir los objetos en formato JSON o YAML y guardarlos como código.

[https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html] (https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

#### ECS CLI

ECS CLI es una versión simplificada de AWS CLI específica para ECS, nos da facilidades para gestionar y acceder a todos los recursos de ECS. Muy recomendable para desarrolladores, facilita las tareas cotidianas

[https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_CLI.html] (https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_CLI.html)


### Creación de un clúster

Podemos crear un clúster a través de la consola web o con AWS CLI. Lo más sencillo es hacerlo a través de la consola web ya que crea todos los demás recursos necesarios, aunque en producción sería bueno automatizarlo con CloudFormation o Terraform.

Debemos elegir un capacity provider para nuetro clúster que no es otra cosa que los sistemas donde se levantarán los contenedores. Pueden ser FARGATE o FARGATE_SPOT para utilziar este servicio, o cualquier autoscaling group que incluya los nodos de nuestro clúster para utilizar máquinas de EC2. Haciéndolo en la consola web, ésta creará todos los recursos necesarios.

Al crear un clúster también se creará automáticamente una **VPC** o red privada virtual, específica para el clúster. También es posible crearlo en una VPC ya existente.

En cualquier caso es importante que la red tenga subnets en **al menos dos zonas de disponibilidad distintas**, y también recomendable que tenga **subnets privadas** para los contenedores y públicas para los balanceadores que recibirán tráfico del exterior, para mantener aislados los servicios privados.

Cómo crear el clúster: [https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create_cluster.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create_cluster.html)

Más sobre networking en AWS: [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html] (https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html)


### Despliegue de los ejercicios

En la carpeta `app-ecs` encontrarás varios archivos para desplegar services y task definitios de ejemplo con la app que hemos creado en las prácticas de Docker

#### 1. Con ECS CLI

Usando ECS CLI podemos definir nuestras tasks en un archivo `docker-compose.yml` y nuestro service en un archivo `ecs-params.yml`

Primero debemos cofigurar el CLI. Creamos un perfil con los datos de nuestro cluster y lo llamamos `bmat-docker`

(Antes debes haber configurado tu cuenta de AWS con tu Access Key y Secret Key)

```
ecs-cli configure --cluster <CLUSTER ECS> --default-launch-type FARGATE --region <REGION> --config-name bmat-docker
```

Debemos sustituir en el archivo `ecs-params.yml` los ID de las subnets y del security group con los específicos de nuestra VPC. Asegúrate de que el security group que utilices tiene el puerto 5000 abierto, para poder acceder a ese puerto en las tasks.

A continuación creamos la task definition y el servicio a partir de `docker-compose.yml` y `ecs-params.yml`:

```
ecs-cli compose --project-name flask-app service up --create-log-groups --ecs-profile bmat-docker
```

Podemos ver las tasks creadas con:

```
ecs-cli compose --project-name flask-app service ps --ecs-profile bmat-docker
```

Y logs logs de una task con:

```
ecs-cli logs --task-id <TASK ID> --follow  --ecs-profile bmat-docker
```

Las tasks creadas tiene IP pública porque así lo hemos especificado en `ecs-params.yml`, si el puerto 5000 está abierto en el security group especificado en `ecs-params.yml`, podremos acceder a nuestro servicio.

#### 2. Con AWS CLI

Con aws CLI crearemos cada objeto a partir de su JSON con todos los parámetros explícitos. Usaremos los archivos `definition.json`, que contiene la task definition, y `service.json` que contiene el service.

Asegúrate de sustituir los IDs de las subnets correspondientes y el nombre del cluster en `service.json`

Creamos la task definition con:

```
aws ecs --region eu-west-2 register-task-definition --cli-input-json file://definition.json
```

Y el service con:

```
aws ecs --region eu-west-2 create-service --cli-input-json file://service.json
```

Podemos ver las tasks creadas:

```
aws ecs list-tasks --region eu-west-2 --cluster bmat-docker
```

### Load Balancers

Al crear un service podemos asignarle un load balancer para que cree un endpoint desde el que los usuarios accederán a nuestra app y repartirá el tráfico entre todas las réplicas.

Se recomienda utilizar el tipo *Application Load Balancer*. El *Network Load Balancer* también es adecuado si necesitamos un rendimiento superior a lo normal. Pero el *Network Load Balancer* es de capa 5 y por tanto no puede ofrecer servicios que el *Application Load Balancer* sí que puede como terminación TLS, añadir seguridad WAF, métricas de errores HTTP, etc.

El *Application Load Balancer* lo debemos crear por separado en la consola web de EC2. 

Los load balancer llevan asociados uno o más target group a los que enviar el tráfico correspondiente según las reglas que le hayamos configurado. Al crear un service en ECS con un load balancer asociado lo que hacemos es simplemente crear un target group que incluirá todas las réplicas de la aplicación. Todo esto se hace al crear el service en la consola de ECS. Sólo debemos asegurarnos de que apunte al puerto que expone nuestra app (el 5000 en nuestro caso).

[https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html)

Aplication Load Balancer:  [https://aws.amazon.com/elasticloadbalancing/application-load-balancer/](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/)

### Autoescalado

El autoescalado en ECS es de dos tipos:

1. De contenedores. Un service se puede configurar para que autoescale el número de réplicas basándose en cualquier métrica de cloudwatch (consumo de memoria, CPU, número de peticiones en un load balancer...).

[https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html)


2. De nodos EC2. En caso de que estemos utilizando máquinas de EC2, estos nodos también deben crearse y destruirse automáticamente para que el escalado sea real. ECS da facilidades para configurar el Autoscaling group y modificar el número de nodos cuando haga falta más capacidad.

[https://docs.aws.amazon.com/AmazonECS/latest/developerguide/asg-capacity-providers.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/asg-capacity-providers.html)

### Despliegues

En un service se puede configurar la política de despliegue de nuevas actualizaciones del service:

* Rolling update: Sustituirá réplica antiguas por las nuevas de una en una (se puede configurar la cadencia de despliegue para que sea más rápida o lenta)

* Blue-green: Desplegará todas las nuevas réplicas antes de destruir las antiguas.

[https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html)

### ECR

ECR (Elastic Container Registry) es el registry privado de AWS. Siempre que usemos ECS será recomendable que nuestras imágenes estén almacenadas en este registry para que las tasks se puedan descargar la imagen lo antes posible. 

Creamos un repositorio en ECR para cada imagen que vayamos a utilizar (dentro del repositorio podemos subir todas las imágenes distintas que queramos utilizando tags diferentes). 

Al crearlo podemos activar las opciones de *Tag immutability* (evitar que las tag se puedan sobreescribir)  y *Scan on push* (paras un escáner de vulnerabilidades a todas las imágenes automáticamente).

Una vez creado el repositorio, debemos configurar nuestro cliente local de docker para que pueda subir imágenes al repositorio:

```
aws ecr get-login-password --region <REGION> | docker login --username AWS --password-stdin <REPOSITORY>
```

Renombrar o construir una imagen que se corresponda con el nombre del repositorio:

```
docker tag flask-app <REPOSITORY>:latest
```

Y subirla con:
```
docker push <REPOSITORY>:latest
```

Es recomendable tener las imágenes en un repositorio en la misma región que el clúster de ECS.

### CloudWatch

CloudWatch es el servicio de monitorización de AWS. En él podremos encontrar todas las métricas del uso de nuestras tasks (uso de CPU, memoria, red, etc.) y también los logs que han generado.

A partir de ellos podemos crear alertas y dashboards para completar la monitorización de los servicios en producción.


### docker-compose + ECS

Las últimas versiones de Docker y docker-compose permiten desplegar directamente en ECS sin necesidad de instalar ni configurar ninguna otra herramienta: [https://docs.docker.com/engine/context/ecs-integration/](https://docs.docker.com/engine/context/ecs-integration/)


