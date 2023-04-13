import pandas as pd
from termcolor import colored
import argparse 
import random

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

    while(not founded) and i<len(acum):
        if acum[i]>randomNumber:
            founded=True
            simulation[max(0, i)]+=1
        i+=1

data['Simulación']=simulation

print(colored('\nDatos en el archivo prob_dist.csv', "magenta"))
print(colored(data, 'cyan'), '\n')

data.to_csv(args.outputFilename, index=False, columns=['Simulación'])


# Getting generated cumulative probabilities from the simulation and calculating max KS distance
if args.pruebaKs:
    print(colored('Prueba KS activada', "magenta"))
    sum = 0
    Ks_distance = []
    for index, row in data.iterrows():
        generated_prob = row['Simulación'] / args.n
        sum += generated_prob
        Ks_distance.append(abs(sum - row['Probabilidad Acum']))

    print(colored(f"Valor del estadistico KS: {round(max(Ks_distance), 4)} \n", "yellow"))



# Getting expected and generated frecuencies and calculating chi squared statistical value  
if args.pruebaJi:
    print(colored('Prueba Ji cuadrado activada', "magenta"))
    deviations = []
    for index, row in data.iterrows():
        expected_frec = row['Probabilidad'] * args.n
        generated_frec = row['Simulación']
        deviations.append(pow(generated_frec - expected_frec, 2) / expected_frec)

    ji2 = sum(deviations)

    print(colored(f"Valor del estadistico Ji Cuadrado: {round (ji2, 4)}", "yellow"))
