# Para este caso hay varios criterios de decisión: Laplace, Wald, Hurwicz, savage
import numpy as np
from termcolor import colored
from tabulate import tabulate as tab

def decide(matrix):
  choices= len(matrix.index)
  nature_statuses= len(matrix.columns)
  analize_by_laplace(matrix, choices, nature_statuses)
  analize_by_wald(matrix)
  analize_by_hurwicz(matrix)
  analize_by_savage(matrix)

  return

def analize_by_laplace(matrix, n, m):
  '''Laplace calculate average of the coeficients of each alternative. 
  And choses the best average.'''
  print(colored("\n\nMetodo de Laplace", 'magenta'))
  averages=[]
  for index, row in matrix.iterrows():
    array= np.array(row)
    averages.append(np.sum(array)/m)
  
  print(colored("\nPromedios de cada alternativa", 'magenta'))
  columns=[]
  for i in range(n):
    columns.append(f'X{i}')
  print(tab([columns,averages], tablefmt='rounded_grid', stralign='center', floatfmt=".2f"))
  
  results= np.array(averages)
  max_index = results.argmax()
  min_index = results.argmin()
  print(colored(f"\nProblema de Beneficios:\nSe recomienda elegir la alternativa {max_index}", 'cyan'))
  print(colored(f"Que presenta un promedio de {results[max_index]}",'cyan'))
  print(colored(f"\nProblema de Costos:\nSe recomienda elegir la alternativa {min_index}", 'light_blue'))
  print(colored(f"Que presenta un promedio de {results[min_index]}",'light_blue'))
  
  return

def analize_by_wald(matrix):
  '''
  Wald asume that the worst is possible to happend. 
  For cases on we're analizing benefits, it's used maxxminy c(x,y)
  For cases of costs, it's used minxmaxy c(x,y)'''
  print(colored("\n\nMetodo de Wald", 'magenta'))
  minx=[]; maxx=[]
  for index, row in matrix.iterrows():
    array= np.array(row)
    minx.append(np.min(array)) # for benefits
    maxx.append(np.max(array)) # for costs
  maxy=np.argmax(minx)
  miny=np.argmin(maxx)
  print(colored(f"\nProblema de Beneficios:\nSe recomienda elegir la alternativa {maxy}", 'cyan'))
  print(colored(f"Que presenta un coeficiente de {minx[maxy]}",'cyan'))
  print(colored(f"\nProblema de Costos:\nSe recomienda elegir la alternativa {miny}", 'light_blue'))
  print(colored(f"Que presenta un coeficiente de {maxx[miny]}",'light_blue'))
  return

def analize_by_hurwicz(matrix):

  return

def analize_by_savage(matrix):

  return