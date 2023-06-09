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
