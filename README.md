# Trabajo Práctico 1

Alumnos: Luz Godoy y Guillermo Arregin

Este repositorio contiene un programa que permite generar valores 
simulados que sigan una determinada distribución de probabilidad.

**NOTA:** 
Es necesario previamente correr los comandos:
> py -m pip install pandas

> pip install argparse

> pip install termcolor


## Cómo ejecutar el script?

> py tp1 prob_dist.csv values.csv n [-d] [-x]

prob_dist.csv -> La primera columna contiene los valores esperados y la segunda las probabilidades. 

n -> Cantidad de valores que se desean generar

d -> Flag para mostrar el estadistico de prueba ks

x -> Flag para mostrar el estadistico de prueba ji cuadrado

Se puede usar la flag -h para mostrar un mensaje de ayuda, que explica como utilizar los parametros.

> py tp1.py -h