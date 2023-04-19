import pandas as pd
from termcolor import colored
import argparse 
import random

parser = argparse.ArgumentParser(
    description=' calcula iterativamente la solución de un problema lineal a partir de su forma matematica estandar, por medio del método simplex.',
)

# Define positional arguments
parser.add_argument('inputFilename', type=str, help='Nombre del archivo csv de entrada para procesar')
parser.add_argument('-m', action='store_true', help='')
parser.add_argument('-M', action='store_true', help='')
