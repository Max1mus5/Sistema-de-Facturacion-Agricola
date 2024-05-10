# Sistema de Facturación Agrícola

## Tabla de Contenidos

- [Parte 1](#estructura-del-proyecto)
- [Parte 2](#añadiendo-interfaces)

## Introducción

Este proyecto es un sistema de facturación diseñado para una tienda agrícola que maneja productos de control (fertilizantes y controles de plagas) y medicina para animales de granja, específicamente antibióticos. El sistema permite gestionar pedidos (o facturas) que están compuestos por los productos que serán comprados, facilitando el proceso de venta y la gestión de inventario.

Para tener una vision mas global ver el diagrama de clases:
<img src="./img/Diagrama de Clases.png">

## Requerimientos

### Prerequisitos

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos:

- Tener instalado Python.

### Instalación

Para instalar el proyecto, sigue estos pasos:

1. Clona el repositorio en tu máquina local.
2. Navega al directorio del proyecto.

## Estructura del Proyecto
<img src="./img/projectStructure.png">

El proyecto está organizado en varios módulos, cada uno con una funcionalidad específica:

- `models/clientModel.py`: Define la clase `Client` para manejar la información de los clientes.
- `models/billModel.py`: Define la clase `Bill` para manejar la información de las facturas.
- `models/antibioticsModel.py`: Define la clase `Antibiotic` para manejar la información de los antibióticos.
- `models/productControlModel.py`: Define la clase `ProductControl` y sus subclases `plague_ProductControl` y `FertilizerProductControl` para manejar la información de los productos de control.

## Uso

El enfoque de esta primera parte del proyecto esta pensada para realizar Test Unitarios, por lo que se ha creado un archivo `main.py` para realizar pruebas de los modelos creados. A continuación, se muestra un ejemplo de cómo utilizar los modelos creados en el proyecto:
  
  ```python
## Pruebas

Para ejecutar las pruebas, navega al directorio de pruebas y ejecuta `python .\main.py`.
```
<img src="./img/tests.png">

se ha realizado un debub para ver la relacion entre los objetos y verificar que se esten creando correctamente ademas de estar relacionados de la forma correcta.

<img src="./img/debug.png">



## Añadiendo Interfaces
para esta parte del proyecto se han añadido interfaces con el fin de aumentar la modularizacion del codigo, asi como su escalabilidad

### *Diagrama de Componentes con Implementacion de Interfaces*
<img src="./img/Diagrama de componentes Con Interfaces.png">

Cabe hacer una aclaración: *el llamado del "Crud" en el Main unicamente tiene como objetivo la "creacion" de la tienda*

Esta seria La Estrucura Del Proyecto con la implementacion de Interfaces
<img src="./img/EstructuraConInterfaces.png">


Corto Ejemplo De como implementamos las interfaces en el proyecto
<img src="./img/Ejemplo Implementacion de Interfaz.png">

## Licencia

Este proyecto fue desarrollado por *Jeronimo Riveros* y *Daniel Rosas* con fines de aprendizaje. Puedes utilizar el código de este proyecto para tus propios fines, pero no puedes utilizarlo con fines comerciales.
