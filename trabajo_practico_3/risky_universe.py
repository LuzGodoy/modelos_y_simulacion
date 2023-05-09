# Sabemos con qué probabilidad ocurren los estados de la naturaleza. 
# Tomamos el coeficiente de cada estado y lo multiplicamos por la probabilidad. 
import numpy as np
from termcolor import colored

def decide(matrix):
  choices= len(matrix.index)-1
  nature_statuses= len(matrix.columns)
  # Save the probabilities in a separated array
  probabilities= matrix.iloc[-1].values
  matrix = matrix.drop(matrix.index[-1])
  expectation=[]
  for index, row in matrix.iterrows():
    expectation.append(get_prom_pond(row, probabilities))
  array= np.array(expectation)
  max_index = array.argmax()
  min_index = array.argmin()
  print(colored(f"Problema de Beneficios:\nSe recomienda elegir la alternativa {max_index}", 'cyan'))
  print(colored(f"Que presenta una esperanza de {array[max_index]}",'cyan'))
  print(colored(f"Problema de Costos:\nSe recomienda elegir la alternativa {min_index}", 'light_red'))
  print(colored(f"Que presenta una esperanza de {array[min_index]}",'light_red'))
  return


def get_prom_pond(row, probabilities):
  sum=0
  for i in range(len(row)):
    sum+=row[i]*probabilities[i]
  
  return sum
