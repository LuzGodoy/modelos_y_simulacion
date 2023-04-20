# Modelos y Simulación

**Alumnos**: Luz Godoy y Guillermo Arregin

**Restricción**: Para correr estos scripts debe usarse `Python3`


## Trabajo Práctico 1

El script `tp1.py` permite generar valores simulados que sigan una determinada distribución de probabilidad.


Es necesario previamente instalar las siguientes librerias:
```
> py -m pip install pandas

> py -m pip install argparse

> py -m pip install termcolor
```

### Cómo ejecutar el script?

```
> py tp1.py prob_dist.csv values.csv n [-d] [-x]
```

| Parametros | Descripción |
| :---: | --- |
| prob_dist.csv | Nombre del archivo csv que contiene en la primera columna contiene los valores esperados y la segunda las probabilidades. |
| values.csv | Nombre del archivo csv que contiene los valores generados. |
| n | Cantidad de valores que se desean generar |
| d | Flag para mostrar el estadistico de prueba ks |
| x | Flag para mostrar el estadistico de prueba ji cuadrado |

Se puede usar el flag -h para mostrar un mensaje de ayuda, que explica como utilizar los parametros.

```
> py tp1.py -h
```

## Trabajo Práctico 2

El script `tp2.py` calcula iterativamente la solución de un problema lineal a partir de su forma matematica estandar, por medio del método simplex. Este script soporta la maximización y la minimización de la función objetivo. No tiene en consideración restricciones que no sean de menor o igual.

Es necesario previamente instalar la siguiente libreria:
```
> py -m pip install tabulate
```

### Cómo ejecutar el script?

```
> py tp2.py model.csv (-m | -M)
```

| Parametros | Descripción |
| :---: | --- |
| model.csv | Nombre del archivo que contiene en la primera fila los coeficientes de la función objetivo y en el resto de las filas los coeficientes técnicos de las restricciones y los términos independientes en la última columna. |
| m | Flag que indica que el problema es de minimización. |
| M | Flag que indica que el problema es de maximización. |

**Nota:** Uno de los dos flags debe estar activado mandatoriamente. 
