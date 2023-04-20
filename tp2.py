import pandas as pd
from termcolor import colored
import argparse 
import csv
import sys
import sympy as sp

"""Calculates cj and cj-zj and returns them as two dicts"""
def getcjzj(targetf, num_res, currentbase, df):
  z = dict()
  cz = dict()
  for var in targetf.keys():
    acum = 0
    for i in range(num_res):
      acum += targetf[currentbase[i]] * df.at[i, var]
    z[var] = acum
    cz[var] = targetf[var] - z[var]
  acum_solution = 0
  for i in range(num_res):
    acum_solution += df.at[i, "Solution"] * targetf[currentbase[i]]
  z["Solution"] = acum_solution
  return z, cz


"""Checks whether the cjzj values meet the finish criteria or not"""
def finished(cz):
  if (args.maximize):
    if (cz[getmaxvar(cz)] <= 0):
      return True
    else:
      return False
  elif (args.minimize):
    if (cz[getminvar(cz)] >= 0):
      return True
    else:
      return False
  

"""Gets maximum value within the cj-zj dict"""
def getmaxvar(cz):
  max = 0
  maxvar = None
  for key in cz.keys():
    if (max != sp.Max(max, cz[key])):
      max = cz[key]
      maxvar = key
  return maxvar


"""Gets minimun value within the cj-zj dict"""
def getminvar(cz):
  min = 0
  minvar = None
  for key in cz.keys():
    if (min != sp.Min(min, cz[key])):
      min = cz[key]
      minvar = key
  return minvar


""""""
# def 



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
  print("minimize activated")
elif (args.maximize):
  print("maximize activated")
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


# Define constant M
M = sp.symbols("M", positive=True) # positive attribute enables Max/Min comparissons


# Standarize restrictions and target function
one_position = 0
for i in range(num_restrictions):
  new_col = f"S{i+1}"
  new_artificial_col = f"A{i+1}"
  data.insert(column=new_col, value=0, loc=len(data.columns))
  data.insert(column=new_artificial_col, value=0, loc=len(data.columns))
  data.at[i, new_col] = -1
  data.at[i, new_artificial_col] = 1
  target_function[new_col] = 0
  target_function[new_artificial_col] = -M
  one_position += 1


# Initialize auxiliar collections
base = dict()
zj = dict()
cjzj = dict()
for i in range(num_restrictions):
  base[i] = f"A{i+1}"
zj, cjzj = getcjzj(target_function, num_restrictions, base, data)


print(data.head())
print(zj)
print(cjzj)
# while not finished(cjzj):
#   if (args.maximize):
#     maxvar = getmaxvar(cjzj)



