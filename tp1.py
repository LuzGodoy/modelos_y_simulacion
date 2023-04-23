import pandas as pd
from termcolor import colored
import argparse 
import random
from tabulate import tabulate as tab
import tp1_utils as utils

parser = argparse.ArgumentParser(
  description='Este script genera valores simulados que sigan una determinada distribución de probabilidad.',
)

# Define positional arguments
parser.add_argument('inputFilename', type=str, help='Nombre del archivo csv de entrada para procesar')
parser.add_argument('outputFilename', type=str, help='Nombre del archivo csv de salida para almacenar los resultados')
parser.add_argument('n', type=int, help='Cantidad de valores aleatorios que se desean generar')

# Define and read optional arguments
parser.add_argument('-d','--pruebaKs', action='store_true', help='Flag para mostrar el estadistico de prueba ks')
parser.add_argument('-x', '--pruebaJi',action='store_true', help='Flag para mostrar el estadistico de prueba ji cuadrado')
args = parser.parse_args()

# Read Comma Separated Value's file
data = pd.read_csv(args.inputFilename, header=None)
data.columns= ['Valor esperado', 'Probabilidad']
data = data.sort_values('Valor esperado', ignore_index= True)

# Calculate the cumulative probability 
acum=[]
sum=0
for prob in data.iloc[:,1]:
  sum+=prob
  acum.append(sum)

data['Probabilidad Acum']=acum

# Generate a list of n random numbers between 0 and 1
random_numbers = []
for _ in range(args.n):
  random_numbers.append(random.random())
print(colored('{} números aleatorios generados'.format(args.n), 'green'))
for number in random_numbers:
  print("{:.2f}".format(number), end= ' ')

# Categorize the generated random numbers according to the cumulative probabilities
simulation= [0] * len(acum)

for random_number in random_numbers:
  i=0
  founded= False
  while(not founded) and i<len(acum):
    if acum[i]>random_number:
      founded=True
      simulation[max(0, i)]+=1
    i+=1

data['Simulación']=simulation
data.to_csv(args.outputFilename, index=False, columns=['Simulación'])

# Calculate the probabilities of the simulated values
sim_probs = []
sim_acum = []
sum = 0
for index, row in data.iterrows():
  prob=row['Simulación']/ args.n
  sim_probs.append(prob)
  sum += prob
  sim_acum.append(sum)

data['Sim Prob']=sim_probs
data['Sim Prob Acum']= sim_acum

# Show complete Data Frame
print("\n")
print(colored('\nDatos en el archivo prob_dist.csv\n', "magenta"))
table, columns = utils.set_table(data)
print(colored(tab(table, columns, tablefmt="grid"), "cyan"))

total_sim= 0
for sim in data['Simulación']:
  total_sim+=sim

# Getting generated cumulative probabilities from the simulation and calculating max KS distance
if args.pruebaKs:
  print(colored('Prueba KS activada', "magenta"))
  ks_distance= utils.test_ks_distance(data)
  print(colored(f"Valor del estadistico KS: {round(max(ks_distance), 4)} \n", "yellow"))

# Getting expected and generated frecuencies and calculating chi squared statistical value  
if args.pruebaJi:
  print(colored('Prueba Ji cuadrado activada', "magenta"))
  ji2= utils.test_chi_squared(data, args.n)
  print(colored(f"Valor del estadistico Ji Cuadrado: {round (ji2, 4)}", "yellow"))
