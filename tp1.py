import pandas as pd
from termcolor import colored
import argparse 

parser = argparse.ArgumentParser(
    description='Genera valores simulados que sigan una determinada distribución de probabilidad',
)

# Argumentos posicionales 
parser.add_argument('filename', type=str, help='Nombre del archivo csv para procesar')

# Argumentos opcionales
parser.add_argument('-d','--pruebaKs', action='store_true', help='Flag para mostrar el estadistico de prueba ks')
parser.add_argument('-x', '--pruebaJi',action='store_true', help='Flag para mostrar el estadistico de prueba ji cuadrado')
args = parser.parse_args()

data = pd.read_csv(args.filename, header=None)
print(colored('\nDatos en el archivo prob_dist.csv', "magenta"))
print(colored(data, 'cyan'), '\n')

if args.pruebaKs:
    print(colored('Prueba KS activada', "magenta"))

if args.pruebaJi:
    print(colored('Prueba Ji cuadrado activada', "magenta"))



# TODO:
# 1. primero leer valores esperados y sus probabilidades 
# ...puede ser en un mapa en el que la key sea el 
# ...valor esperado y la probabilidad sea el value. 
# ...por que el v.e. no se repite pero la probabilidad 
# ...si se puede repetir
# 1.1. opc. ordenar el mapa por valores esperados

# 2. sacar las probabilidades acumuladas
# 3. saco n numeros aleatorios para la simulación
# 4. iterar entre los datos simulados, categorizandolos 
# segun el rango de la probabilida correspondiente.


