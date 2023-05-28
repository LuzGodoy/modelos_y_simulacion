'''Este script resuelve un problema de decisión a partir de la matriz de compensaciones.'''
import argparse
import pandas as pd
from termcolor import colored
import risky_universe as risk_algorithm
import uncertain_universe as uncertain_algorithm
import conflict_universe as conflict_algorithm
import common_utils as utils

parser = argparse.ArgumentParser(
    description='Resuelve un problema de decisión a partir de la matriz de compensaciones.',
)

# Define and read the script's arguments
parser.add_argument(
    'inputFile',
    type=str,
    help='Nombre del archivo csv con la matriz de compensaciones.',
)

parser.add_argument(
    '-r',
    '--risk',
    action='store_true',
    help='Indica que el problema de decisión es en condiciones de riesgo.',
)
parser.add_argument(
    '-u',
    '--uncertain',
    action='store_true',
    help='Indica que el problema de decisión es en condiciones de incertidumbre.',
)
parser.add_argument(
    '-i',
    '--coeficient',
    type=float,
    help='Coeficiente del criterio de Hurwicz en condiciones de incertidumbre.',
)
parser.add_argument(
    '-c',
    '--conflict',
    action='store_true',
    help='Indica que el problema de decisión es en condiciones de conflicto.',
)

args = parser.parse_args()
if args.uncertain and args.coeficient is None:
    parser.error(
        '''Debe especificar un valor para el coeficiente de Hurwicz si 
        declara que el problema es en condiciones de incertidumbre''',
    )

matrix = pd.read_csv(args.inputFile, header=None)
columns= uncertain_algorithm.name_columns(len(matrix.columns))

if args.risk:
    print(colored("Problema de decision condiciones de riesgo", 'magenta'))
    utils.print_table(matrix, columns)
    risk_algorithm.decide(matrix)
elif args.uncertain:
    print(colored("Problema de decision condiciones de incertidumbre", 'magenta'))
    utils.print_table(matrix, columns)
    uncertain_algorithm.decide(matrix, args.coeficient)
elif args.conflict:
    print(colored("Problema de decision condiciones de  conflicto", 'magenta'))
    utils.print_table(matrix, columns)
    conflict_algorithm.decide(matrix)
