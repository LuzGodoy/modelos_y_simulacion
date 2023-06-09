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