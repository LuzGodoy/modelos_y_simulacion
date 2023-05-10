import pandas as pd
from termcolor import colored
import argparse 
from tabulate import tabulate as tab

import risky_universe as risk_algorithm
import uncertain_universe as uncertain_algorithm
import conflict_universe as conflict_algorithm

parser = argparse.ArgumentParser(description='Este script resuelve un problema de decisión a partir de la matriz de compensaciones.')

# Define and read the script's arguments
parser.add_argument('inputFile', type=str, help='Nombre del archivo csv con la matriz de compensaciones.')

parser.add_argument('-r', '--risk', action='store_true', help='Indica que el problema de decisión es en condiciones de riesgo.')
parser.add_argument('-u', '--uncertain', action='store_true', help='Indica que el problema de decisión es en condiciones de incertidumbre.')
parser.add_argument('-i','--coeficient', type=int, help='Coeficiente del criterio de Hurwicz para un problema de decisión en condiciones de incertidumbre.')
parser.add_argument('-c', '--conflict', action='store_true', help='Indica que el problema de decisión es en condiciones de conflicto.')

args = parser.parse_args()
if args.uncertain and args.coeficient is None:
  parser.error("Debe especificar un valor para el coeficiente de Hurwicz si declara que el problema es en condiciones de incertidumbre")

matrix = pd.read_csv(args.inputFile, header=None)

if args.risk: 
  print(colored("Problema de decision condiciones de riesgo", 'magenta'))
   # TODO: add headers for the nature statuses and decision alternatives to print them in the table below, and diferenciate the probabilities
  print(tab(matrix, tablefmt='rounded_grid', showindex=False))
  risk_algorithm.decide(matrix)
elif args.uncertain:
  print(colored("Problema de decision condiciones de incertidumbre", 'magenta'))
  # TODO: add headers for the nature statuses and decision alternatives to print them in the table below
  print(tab(matrix, tablefmt='rounded_grid', showindex=False))
  uncertain_algorithm.decide(matrix)
elif args.conflict:
  print(colored("Problema de decision condiciones de  conflicto", 'magenta'))
  conflict_algorithm.decide(matrix)
