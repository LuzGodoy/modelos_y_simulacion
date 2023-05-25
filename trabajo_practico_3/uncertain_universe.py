# Para este caso hay varios criterios de decisión: Laplace, Wald, Hurwicz, savage
import numpy as np
from termcolor import colored
from tabulate import tabulate as tab
import pandas as pd

def decide(matrix, coef):
  choices, nature_statuses= matrix.shape
  analize_by_laplace(matrix, choices, nature_statuses)
  analize_by_wald(matrix)
  analize_by_hurwicz(matrix, coef)
  analize_by_savage(matrix, choices, nature_statuses)

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
  columns=columns= name_columns(n)
  print(tab([columns,averages], tablefmt='rounded_grid', stralign='center', floatfmt=".2f"))
  
  results= np.array(averages)
  max_index = results.argmax()
  min_index = results.argmin()

  # Results
  print(colored(f"\nProblema de Beneficios:\nSe recomienda elegir la alternativa {max_index}", 'cyan'))
  print(colored(f"Que presenta un promedio de {results[max_index]}",'cyan'))
  print(colored(f"\nProblema de Costos:\nSe recomienda elegir la alternativa {min_index}", 'light_blue'))
  print(colored(f"Que presenta un promedio de {results[min_index]}",'light_blue'))
  
  return

def analize_by_wald(matrix):
  '''
  Wald asume that the worst is possible to happend. 
  For cases on we're analizing benefits, it's used maxxminy c(x,y)
  For cases of costs, it's used minxmaxy c(x,y)
  '''
  print(colored("\n\nMetodo de Wald", 'magenta'))
  minx=[]; maxx=[]
  for index, row in matrix.iterrows():
    array= np.array(row)
    minx.append(np.min(array)) # for benefits
    maxx.append(np.max(array)) # for costs
  maxy=np.argmax(minx)
  miny=np.argmin(maxx)

  # Results
  columns= name_columns(len(matrix.index))
  print(colored(f"\nProblema de Beneficios:\nSe recomienda elegir la alternativa {maxy}", 'cyan'))
  print(colored(f"Que presenta un coeficiente de {minx[maxy]}",'cyan'))
  print(colored(f"Tabla de minimos",'cyan'))
  print(tab([columns,minx], tablefmt='rounded_grid', stralign='center', floatfmt=".2f"))

  print(colored(f"\nProblema de Costos:\nSe recomienda elegir la alternativa {miny}", 'light_blue'))
  print(colored(f"Que presenta un coeficiente de {maxx[miny]}",'light_blue'))
  print(colored(f"Tabla de maximos",'light_blue'))
  print(tab([columns,maxx], tablefmt='rounded_grid', stralign='center', floatfmt=".2f"))
  
  return

def analize_by_hurwicz(matrix, coef):
  '''
  Benefits ⇒ d(x) = α · maxy c(x, y) + (1 − α) · miny c(x, y)
  Costs ⇒ d(x) = α · miny c(x, y) + (1 − α) · max y c(x, y)
  '''
  print(colored("\n\nMetodo de Hurwicz", 'magenta'))
  complement= 1-coef
  benefits= []; costs=[]
  for index, row in matrix.iterrows():
    array= np.array(row)
    miny=np.min(array)
    maxy=np.max(array)
    benefits.append(coef*maxy + complement*miny)
    costs.append(coef*miny + complement*maxy)
  benefits= np.array(benefits)
  costs= np.array(costs)
  benefit= np.argmax(benefits)
  cost=np.argmin(costs)

  # Results
  columns=name_columns(len(matrix.index))
  print(colored(f"\nProblema de Beneficios:\nSe recomienda elegir la alternativa {benefit}", 'cyan'))
  print(colored(f"Que presenta un coeficiente de {benefits[benefit]}",'cyan'))
  print(colored(f"Promedios ponderados",'cyan'))
  print(tab([columns,benefits], tablefmt='rounded_grid', stralign='center', floatfmt=".2f"))

  print(colored(f"\nProblema de Costos:\nSe recomienda elegir la alternativa {cost}", 'light_blue'))
  print(colored(f"Que presenta un coeficiente de {costs[cost]}",'light_blue'))
  print(colored(f"Promedios ponderados",'light_blue'))
  print(tab([columns,costs], tablefmt='rounded_grid', stralign='center', floatfmt=".2f"))

  return

def analize_by_savage(matrix, rows, columns):
  ''' '''
  print(colored("\n\nMetodo de Savage", 'magenta'))
  benef_matrix, costs_matrix = generate_regret_matrixes(matrix, rows, columns)
  columns= name_columns(rows)

  # For benefits
  index, coef= wald_costs(benef_matrix)
  print(colored(f"\nProblema de Beneficios:\nSe recomienda elegir la alternativa {index}", 'cyan'))
  print(colored(f"Que presenta un coeficiente de {coef}",'cyan'))
  print(colored(f"Matriz de arrepentimiento para beneficios",'cyan'))
  print(tab(benef_matrix, tablefmt='rounded_grid', stralign='center', floatfmt=".2f"))
  
  # For costs
  index, coef= wald_costs(costs_matrix)
  print(colored(f"\nProblema de Costos:\nSe recomienda elegir la alternativa {index}", 'light_blue'))
  print(colored(f"Que presenta un coeficiente de {coef}",'light_blue'))
  print(colored(f"Matriz de arrepentimiento para costos",'light_blue'))
  print(tab(costs_matrix, tablefmt='rounded_grid', stralign='center', floatfmt=".2f"))

  return

def wald_costs(matrix):
  ''' It returns the index of the minymaxx 
  (the number of the suggested selected choice)
  along with the selected coeficient.
  '''
  maxx=[]
  for index, row in matrix.iterrows():
    array= np.array(row)
    maxx.append(np.max(array))
  miny=np.argmin(maxx)

  return miny, maxx[miny]

def generate_regret_matrixes(matrix, rows, columns):
  '''This method returns both regret matrixes, 
  one for benefits and another for costs, 
  given a [matrix] passed by parameter
  '''
  benef_regret= pd.DataFrame(columns=range(columns))
  costs_regret=pd.DataFrame(columns=range(columns))
  max_col=[]; min_col=[]
  for column_name in matrix.columns:
    column_data=matrix[column_name]
    max_col.append(column_data.max()) 
    min_col.append(column_data.min())
  
  for i in range(rows):
    benef_row = []
    costs_row = []
    for j in range(columns):
      element= matrix.iloc[i, j]
      benef_row.append(max_col[j] - element)
      costs_row.append(element - min_col[j])
    benef_regret.loc[i] = benef_row
    costs_regret.loc[i] = costs_row
  
  return benef_regret, costs_regret

def name_columns(n):
  columns=[]
  for i in range(n):
    columns.append(f'X {i}')

  return columns