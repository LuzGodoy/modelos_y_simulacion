# Trabajo Práctico 1

Alumnos: Luz Godoy y Guillermo Arregin

**NOTA:** 
Es necesario previamente correr los comandos:
> py -m pip install pandas

> pip install termcolor

Un programa que permite generar valores simulados que sigan una
determinada distribución de probabilidad.

## Cómo ejecutar el script?

> py tp1 prob_dist.csv values.csv n [-d] [-x]

prob_dist.csv     col1->ValoresEsperados     col2->Probabilidades

n -> Cantidad de valores que se desean generar

d -> Flag para mostrar el estadistico de prueba ks

x -> Flag para mostrar el estadistico de prueba ji cuadrado