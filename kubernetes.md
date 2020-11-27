# Kubernetes

<img src="img/kubernetes.png" alt="kubernetes" width="600px">

Es un **orquestador de contenedores** como ECS:

- Administra el despliegue de contenedores
- Preparado para entornos de producción
- De código abierto

Kubernetes dispone de herramientas para levantar contenedores:

- En alta disponibilidad
- De forma segura
- Aislados de otras cargas de trabajo
- Conectados entre sí
- Expuestos a Internet
- Conectados con servicios en la nube

## Links de introducción

- [¿Qué es Kubernetes? Web oficial](https://kubernetes.io/es/docs/concepts/overview/what-is-kubernetes/)
- [Cómic](https://cloud.google.com/kubernetes-engine/kubernetes-comic)
- [Guía ilustrada](https://www.cncf.io/wp-content/uploads/2020/08/The-Illustrated-Childrens-Guide-to-Kubernetes.pdf)

## Instala Kubernetes en local
- [Windows](https://docs.docker.com/docker-for-windows/#kubernetes)
- [Mac](https://docs.docker.com/docker-for-mac/#kubernetes)
- [Linux](https://microk8s.io/)

## AWS
AWS dispone de un servicio de Kubernetes gestionado: EKS [https://aws.amazon.com/eks/](https://aws.amazon.com/eks/)

## Manos a la obra

En Kubernetes todas las operaciones se realizan con el comando `kubectl`:

Crear (y actualizar) objetos a partir de archivos YAML: `kubectl apply -f <ARCHIVO>`

Listar objetos: `kubectl get <OBJETO>`. Por ejemplo: `kubectl get pod`

Ver detalles de un objeto en concreto: `kubectl get <OBJETO> <NOMBRE> -o yaml`. Por ejemplo: `kubectl get pod nginx -o yaml`

Eliminar un objeto en concreto: `kubectl delete <OBJETO> <NOMBRE>`


#### Objetos

Puedes encontrar todas las definiciones de los objetos que veremos en la carpeta `kubernetes`

##### Nodos

Son los servidores físicos que forman parte del clúster.

Lista todos los nodos con `kubectl get nodes`

##### Pod

Un Pod en Kubernetes es un objeto que define una **carga de trabajo**. Es decir, un Pod es uno o varios contenedores que son ejecutados conjuntamente en Kubernetes. Se corresponde con una task de ECS.

Crea un pod con `kubectl apply -f pod.yaml`

Lista todos los pod con `kubectl get pod`

Ver la descripción del pod:  `kubectl describe pod nginx`

##### Deployments

El objeto Deployment define una aplicación con varias réplicas. El Deployment a su vez crea y gestiona los pods que corresponden a esa definición. Se corresponde con un service de ECS

Crea un deployment con `kubectl apply -f deployment.yaml`

Lista todos los deployment con `kubectl get deploy`

##### Service
Service representa un balanceador de carga entre varios pods que comparten una misma etiqueta, normalmente entre las réplicas de un mismo deployment. Se corresponde con un load balancer de AWS

Crea un service con `kubectl apply -f service.yaml`

Lista todos los service con `kubectl get service`
