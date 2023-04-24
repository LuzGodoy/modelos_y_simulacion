import pandas as pd
from termcolor import colored
import argparse 
import csv
import sys
import simplex_utils as utils
from tabulate import tabulate as tab

parser = argparse.ArgumentParser(
    description='Este script calcula iterativamente la solución de un problema lineal a partir de su forma matematica estandar, por medio del método simplex.',
)

# Define positional arguments
parser.add_argument('inputFilename', type=str, help='Nombre del archivo csv de entrada para procesar')

group = parser.add_mutually_exclusive_group()
group.add_argument('-m', '--minimize', action='store_true', help='Indica que el problema es de minimizacion')
group.add_argument('-M', '--maximize', action='store_true', help='Indica que el problema es de maximizacion')

args = parser.parse_args()
if (args.minimize):
  print(colored("La función objetivo se manimizará.", 'magenta'))
elif (args.maximize):
  print(colored("La función objetivo se maximizará.", 'magenta'))
else:
  print(colored("Una de las flags -M o -m debe estar activada.", 'magenta'))
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
base = dict(); zj = dict(); cjzj = dict()
for i in range(num_restrictions):
  base[i] = f"S{i+1}"
zj, cjzj = utils.get_cjzj(target_function, num_restrictions, base, data)

# Show the table with the values of the initialization 
print(colored('\nFase de Inicialización', 'magenta'))
table, columns = utils.set_table(num_restrictions, data, target_function, base, zj, cjzj)
print(colored(tab(table, columns, tablefmt="grid"), 'cyan'))

# Start iterations
iterations = 0
cjzj_history = []
while not utils.is_finished(cjzj, args):
  iterations += 1
  if (args.maximize):
    selected_column = utils.get_max_var(cjzj)
    replace_index = utils.min_exit_base(num_restrictions, data, selected_column)
    if replace_index == None:
      print(colored(f"\nLa simulación terminó debido a que no hay pivotes positivos", "red"))
      break
  elif (args.minimize):
    selected_column = utils.get_min_var(cjzj)
    replace_index = utils.min_exit_base(num_restrictions, data, selected_column)
    if replace_index == None:
      print(colored(f"\nLa simulación terminó debido a que no hay pivotes positivos", "red"))
      break
  data, base = utils.replace_base(selected_column, replace_index, base, data)
  data = utils.update_values(selected_column, replace_index, base, data)
  zj, cjzj = utils.get_cjzj(target_function, num_restrictions, base, data)
  print(colored(f"\nIteracion: {iterations}", 'magenta'))
  table, columns = utils.set_table(num_restrictions, data, target_function, base, zj, cjzj)
  print(colored(tab(table, columns, tablefmt="grid"), 'cyan'))
  if ((base,cjzj) in cjzj_history):
    print(colored(f"\nLa simulación terminó debido a un ciclo infinito", "red"))
    break
  else:
    cjzj_history.append((base,cjzj))

print(colored(f"\nLa simulacion terminó en {iterations} iteraciones\n", "yellow"))
