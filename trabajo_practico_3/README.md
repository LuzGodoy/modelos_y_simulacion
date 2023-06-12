
## Trabajo Práctico 3

El script `tp3.py` resuelve un problema de decisión a partir de la matriz de compensaciones. 

* En **condiciones de riesgo**, se muestra el número de alternativa que debería tomar el decisor de acuerdo a las probabilidades para cada posible estado de la naturaleza, tanto para beneficios como para costos.

* En **condiciones de incertidumbre**, se muestra el número de alternativa que debería tomar el decisor para cada uno de los cuatro criterios (Laplace, Wald, Hurwicz, savage), tanto para beneficios como para costos.

* En **condiciones de conflicto**, se indica si el juego se puede resolver con una estrategia pura óptima Además se muestra el número de alternativa que debería tomar el decisor, el número de alternativa que seleccionaría el oponente y el valor de juego correspondiente.


### Cómo ejecutar el script?

```
py tp3.py matrix.csv ( -r | -u -i α | -c )
```

| Parametros | Descripción |
| :---: | --- |
| matrix.csv | Nombre del archivo csv que contiene la matriz de compensaciones del problema de decisión. |
| r | Flag que indica que el problema de decisión es en condiciones de riesgo. |
| u | Flag que indica que el problema de decisión es en condiciones de incertidumbre. |
| i | Flag que indica que a continuación se añadirá el  coeficiente del criterio de Hurwicz para un problema de decisión en condiciones de incertidumbre. |
| c | Flag que indica que el problema de decisión es en condiciones de conflicto. |