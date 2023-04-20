import pandas as pd
from termcolor import colored
import argparse 
import csv
import sys
import simplex_utils as utils
from tabulate import tabulate as tab

parser = argparse.ArgumentParser(
    description=' calcula iterativamente la solución de un problema lineal a partir de su forma matematica estandar, por medio del método simplex.',
)

# Define positional arguments
parser.add_argument('inputFilename', type=str, help='Nombre del archivo csv de entrada para procesar')

group = parser.add_mutually_exclusive_group()
group.add_argument('-m', '--minimize', action='store_true', help='Indica que el problema es de minimizacion')
group.add_argument('-M', '--maximize', action='store_true', help='Indica que el problema es de maximizacion')

args = parser.parse_args()

if (args.minimize):
  print(colored("Minimización Activada", 'magenta'))
elif (args.maximize):
  print(colored("Maximización Activada", 'magenta'))
else:
  print("-M or -m flag is required")
  sys.exit()



# Read CSV's first row for target function
with open(args.inputFilename, newline='') as f:
  reader = csv.reader(f)
  target_coef = next(reader)
  target_function = dict()      
for i in range(len(target_coef)):
  target_function[f"X{i+1}"] = int(target_coef[i])
  

# Read Comma Separated Value's file for restrictions and get amount of variables
data = pd.read_csv(args.inputFilename, header=None, skiprows=1)
num_variables = len(data.columns)-1
num_restrictions = len(data.index)
var_names = []
for i in range(num_variables):
  var_names.append(f"X{i+1}")
var_names.append("Solution")
data.columns = var_names


# Standarize restrictions and target function
one_position = 0
for i in range(num_restrictions):
  new_col = f"S{i+1}"
  data.insert(column=new_col, value=0, loc=len(data.columns))
  data.at[i, new_col] = 1
  target_function[new_col] = 0
  one_position += 1


# Initialize auxiliar collections
base = dict()
zj = dict()
cjzj = dict()
for i in range(num_restrictions):
  base[i] = f"S{i+1}"
zj, cjzj = utils.getcjzj(target_function, num_restrictions, base, data)



iterations = 0
while not utils.finished(cjzj, args):
  iterations += 1
  if (args.maximize):
    selected_column = utils.getmaxvar(cjzj)
    replace_index = utils.minexitbase(num_restrictions, data, selected_column)
  elif (args.minimize):
    selected_column = utils.getminvar(cjzj)
    replace_index = utils.maxexitbase(num_restrictions, data, selected_column)
  data, base = utils.replacebase(selected_column, replace_index, base, data)
  data = utils.updatevalues(selected_column, replace_index, base, data)
  zj, cjzj = utils.getcjzj(target_function, num_restrictions, base, data)
  print(f"\n\nIteracion: {iterations}")
  table, columns = utils.settable(num_restrictions, data, target_function, base, zj, cjzj)
  print(tab(table, columns, tablefmt="grid"))

print(colored(f"\nLa simulacion terminó en {iterations} iteraciones\n", "yellow"))




