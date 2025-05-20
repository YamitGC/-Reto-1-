Reto 1 - Simulación de un Proyecto de Investigación Científica en Python

Introducción

Este proyecto, desarrollado como parte del curso "Python de Cero a Senior: La Ruta Maestra del Código", simula un sistema de gestión para un proyecto de investigación científica. La aplicación, basada en consola, permite la recopilación, análisis y manipulación de datos experimentales de un laboratorio ficticio.

El objetivo principal es aplicar conceptos fundamentales de programación en Python, como:

* Estructuras de control de flujo
* Funciones
* Manipulación de datos
* Listas

...para gestionar información científica de manera práctica.

## Funcionalidades Principales

El sistema implementa las siguientes funcionalidades:

1.  **Recopilación de Datos Experimentales:**
    * Permite agregar nuevos experimentos al sistema, registrando detalles como:
        * Nombre del experimento
        * Fecha de realización
        * Tipo de experimento (e.g., Química, Biología, Física)
        * Resultados obtenidos (datos numéricos)
    * Permite visualizar la lista de experimentos registrados.
    * Permite actualizar los resultados de un experimento existente.
    * Permite eliminar un experimento del sistema.

2.  **Análisis de Datos:**
    * Implementa funciones para realizar cálculos estadísticos básicos sobre los resultados de los experimentos, como:
        * Promedio
        * Valor máximo
        * Valor mínimo
    * Permite comparar los resultados entre diferentes experimentos.

3.  **Generación de Informes:**
    * Genera informes resumidos que incluyen:
        * Detalles de cada experimento
        * Análisis de los resultados
        * Conclusiones (opcional)
    * Permite exportar los informes a archivos de texto.

## Instrucciones de Uso

1.  **Requisitos Previos:**
    * Python 3.x instalado.

2.  **Instalación:**
    * No se requiere instalación. Simplemente clona o descarga el repositorio.

3.  **Ejecución:**
    * Ejecuta el script principal de Python (e.g., `main.py`) desde la consola.
    * El programa mostrará un menú de opciones.
    * Sigue las instrucciones en la consola para interactuar con el sistema.

## Estructura del Proyecto

El proyecto está organizado en los siguientes módulos/funciones principales:

* `agregar_experimento()`: Función para agregar un nuevo experimento.
* `ver_experimentos()`: Función para visualizar los experimentos registrados.
* `actualizar_resultados_experimento()`: Función para actualizar los resultados de un experimento.
* `eliminar_experimento()`: Función para eliminar un experimento.
* `generar_informe()`: Función para generar un informe de los experimentos.
* Funciones auxiliares para validación de datos y cálculos estadísticos.

## Consideraciones Adicionales

* Se implementó validación de datos para asegurar la integridad de la información ingresada por el usuario.
* Se utilizó manejo de errores para hacer el programa más robusto.
* El código está comentado para facilitar la comprensión.

## Autor

\ Yamit García / 

## Agradecimientos

Agradecemos al equipo docente del curso "Python de Cero a Senior: La Ruta Maestra del Código" por su guía y apoyo.
