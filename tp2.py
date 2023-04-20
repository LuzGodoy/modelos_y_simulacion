import pandas as pd
from termcolor import colored
import argparse 
import csv

parser = argparse.ArgumentParser(
    description=' calcula iterativamente la solución de un problema lineal a partir de su forma matematica estandar, por medio del método simplex.',
)

# Define positional arguments
parser.add_argument('inputFilename', type=str, help='Nombre del archivo csv de entrada para procesar')
parser.add_argument('-m', action='store_true', help='')
parser.add_argument('-M', action='store_true', help='')

args = parser.parse_args()

# Read CSV's first row for target function
with open(args.inputFilename, newline='') as f:
  reader = csv.reader(f)
  target_coef = next(reader)    # target_function coefficients stored as a list
  target_function = dict()
for i in range(len(target_coef)):
  target_function[f"X{i+1}"] = target_coef[i]
  

# Read Comma Separated Value's file for restrictions and get amount of variables
data = pd.read_csv(args.inputFilename, header=None, skiprows=1)
num_variables = len(data.columns)-1
var_names = []
for i in range(num_variables):
  var_names.append(f"X{i+1}")
var_names.append("coefficient")
data.columns = var_names


# Standarize restrictions and target function
one_position = 0
for i in range(num_variables):
  new_col = f"S{i+1}"
  new_artificial_col = f"A{i+1}"
  data.insert(column=new_col, value=0, loc=len(data.columns))
  data.insert(column=new_artificial_col, value=0, loc=len(data.columns))
  data.at[i, new_col] = -1
  data.at[i, new_artificial_col] = 1
  target_function[new_col] = 0
  target_function[new_artificial_col] = f"M{i+1}"
  one_position += 1


  
print(data.head())
print("\n")
print(target_function)


