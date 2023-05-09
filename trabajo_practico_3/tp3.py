import pandas as pd
from termcolor import colored
import argparse 
import risky_universe as risk_algorithm
import uncertain_universe as uncertain_algorithm
import conflict_universe as conflict_algorithm

parser = argparse.ArgumentParser(description='Este script resuelve un problema de decisión a partir de la matriz de compensaciones.')

# Define and read the script's arguments
parser.add_argument('inputFile', type=str, help='Nombre del archivo csv con la matriz de compensaciones.')
group = parser.add_mutually_exclusive_group()
group.add_argument('-r', '--risk', action='store_true', help='Indica que el problema de decisión es en condiciones de riesgo.')
group.add_argument('-u', '--uncertain', action='store_true', help='Indica que el problema de decisión es en condiciones de incertidumbre.')
group.add_argument('-c', '--conflict', action='store_true', help='Indica que el problema de decisión es en condiciones de conflicto.')

# ! ISSUE: lanza una excepcion al agregar este argumento. Sea opcional o de posicion
# parser.add_argument('-h','--hurwicz', type=int, help='Coeficiente del criterio de Hurwicz para un problema de decisión en condiciones de incertidumbre.')

args = parser.parse_args()
if args.uncertain and args.coeficient is None:
  parser.error("Debe especificar un valor para el coeficiente de Hurwicz si declara que el problema es en condiciones de incertidumbre")

if args.risk: 
  print(colored("Problema de decision condiciones de riesgo", 'magenta'))
  matrix = pd.read_csv(args.inputFile, header=None)
  print(matrix)
  risk_algorithm.decide(matrix)
elif args.uncertain:
  uncertain_algorithm.decide()
elif args.conflict:
  conflict_algorithm.decide()
