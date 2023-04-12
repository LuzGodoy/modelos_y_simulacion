import pandas as pd
from termcolor import colored
import argparse 
import random

parser = argparse.ArgumentParser(
    description='Este script genera valores simulados que sigan una determinada distribución de probabilidad.',
)

# Define positional arguments
parser.add_argument('filename', type=str, help='Nombre del archivo csv para procesar')
parser.add_argument('n', type=int, help='Cantidad de valores aleatorios que se desean generar')

# Define and read optional arguments
parser.add_argument('-d','--pruebaKs', action='store_true', help='Flag para mostrar el estadistico de prueba ks')
parser.add_argument('-x', '--pruebaJi',action='store_true', help='Flag para mostrar el estadistico de prueba ji cuadrado')
args = parser.parse_args()

# Read Comma Separated Value's file
data = pd.read_csv(args.filename, header=None)
data.columns= ['Valor esperado', 'Probabilidad']
data = data.sort_values('Valor esperado', ignore_index= True)

# Calculate the cumulative probability 
acum=[]
sum=0
for prob in data.iloc[:,1]:
    sum+=prob
    acum.append(round(sum, 2))

data['Probabilidad Acum']=acum

# Generate a list of n random numbers between 0 and 1
randomNumbers = []
for _ in range(args.n):
    randomNumbers.append(random.random())
print(colored('{} números aleatorios generados'.format(args.n), 'green'))
for number in randomNumbers:
    print("{:.2f}".format(number), end= ' ')

# Categorize the generated random numbers according to the cumulative probabilities
simulation= [0] * len(acum)
for randomNumber in randomNumbers:
    i=0
    founded= False
    while(not founded):
        if acum[i]>randomNumber:
            founded=True
            simulation[max(0, i)]+=1
        i+=1

data['Simulación']=simulation

print(colored('\nDatos en el archivo prob_dist.csv', "magenta"))
print(colored(data, 'cyan'), '\n')

if args.pruebaKs:
    print(colored('\n\nPrueba KS activada', "magenta"))
# TODO: Hacer la prueba KS y mostrar el resultado

if args.pruebaJi:
    print(colored('Prueba Ji cuadrado activada', "magenta"))
# TODO: Hacer la Prueba Ji Cuadrado y mostrar el resultado
