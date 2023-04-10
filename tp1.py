from sys import argv
import pandas as pd
from termcolor import colored
import argparse

script, filename = argv
data = pd.read_csv(filename, header=None)

print(colored('\nDatos en el archivo prob_dist.csv', "magenta"))
print(colored(data, 'cyan'))

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


