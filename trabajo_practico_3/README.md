
## Trabajo Práctico 3

El script `tp3.py` resuelve un problema de decisión a partir de la matriz de compensaciones. 

* En condiciones de riesgo, el número de alternativa (1 a n) que debería tomar el decisor de
acuerdo a las probabilidades para cada posible estado de la naturaleza, tanto para
beneficios como para costos.

* En condiciones de incertidumbre, el número de alternativa (1 a n) que debería tomar el
decisor para cada uno de los cuatro criterios vistos en la teoría, tanto para beneficios como
para costos.

* En condiciones de conflicto, si el juego se puede resolver con una estrategia pura óptima,
el número de alternativa (1 a n) que debería tomar el decisor, el número de alternativa (1 a
m) que seleccionaría el oponente y el valor de juego correspondiente.


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