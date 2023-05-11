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

> py -m pip install tabulate
```

### Cómo ejecutar el script?

```
> py tp1.py prob_dist.csv values.csv n [-d] [-x]
```

**Nota**: Los corchetes indican que es un parametro opcional. Ninguno, uno o ambos parametros pueden añadirse.

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
> py -m pip install pandas

> py -m pip install argparse

> py -m pip install termcolor

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


## Trabajo Práctico 3

El script `tp3.py` resuelve un problema de decisión a partir de la matriz de compensaciones. 

* En **condiciones de riesgo**, se muestra el número de alternativa que debería tomar el decisor de acuerdo a las probabilidades para cada posible estado de la naturaleza, tanto para beneficios como para costos.

* En **condiciones de incertidumbre**, se muestra el número de alternativa que debería tomar el decisor para cada uno de los cuatro criterios (Laplace, Wald, Hurwicz, savage), tanto para beneficios como para costos.

* En **condiciones de conflicto**, se indica si el juego se puede resolver con una estrategia pura óptima Además se muestra el número de alternativa que debería tomar el decisor, el número de alternativa que seleccionaría el oponente y el valor de juego correspondiente.


### Cómo ejecutar el script?

```
tp3 matrix.csv ( -r | -u α | -c )
```

| Parametros | Descripción |
| :---: | --- |
| matrix.csv | Nombre del archivo csv que contiene la matriz de compensaciones del problema de decisión. |
| r | Flag que indica que el problema de decisión es en condiciones de riesgo. |
| u | Flag que indica que el problema de decisión es en condiciones de incertidumbre. |
| α | Coeficiente del criterio de Hurwicz para un problema de decisión en condiciones de incertidumbre. |
| c | Flag que indica que el problema de decisión es en condiciones de conflicto. |
