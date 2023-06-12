'''Para este caso hay varios criterios de decisión: Laplace, Wald, Hurwicz, savage'''
import numpy as np
from termcolor import colored
import common_utils as utils
import pandas as pd

def decide(matrix, coef):
    '''This method uses the 3 ways to analyze a problem in an uncertain universe.'''
    choices, nature_statuses = matrix.shape
    analize_by_laplace(matrix, choices, nature_statuses)
    analize_by_wald(matrix)
    analize_by_hurwicz(matrix, coef)
    analize_by_savage(matrix, choices, nature_statuses)

def analize_by_laplace(matrix, rows, num_col):
    '''Laplace calculate average of the coeficients of each alternative. 
    And choses the best average.'''
    print(colored("\n\nMetodo de Laplace", 'magenta'))
    averages = []
    for _, row in matrix.iterrows():
        array = np.array(row)
        averages.append(np.sum(array)/num_col)

    print(colored("\nPromedios de cada alternativa", 'magenta'))
    rows_names =  name_rows(rows)
    utils.print_table([rows_names, averages])

    results = np.array(averages)
    max_index = results.argmax()
    min_index = results.argmin()

    # Results
    print(colored(f"\nProblema de Beneficios:\nSe recomienda elegir la alternativa {max_index}", 'cyan'))
    print(colored(f"Que presenta un promedio de {results[max_index]}", 'cyan'))
    print(colored(f"\nProblema de Costos:\nSe recomienda elegir la alternativa {min_index}", 'light_blue'),)
    print(colored(f"Que presenta un promedio de {results[min_index]}", 'light_blue'))

def analize_by_wald(matrix):
    '''
    Wald asume that the worst is possible to happend. 
    For cases on we're analizing benefits, it's used maxxminy c(x,y)
    For cases of costs, it's used minxmaxy c(x,y)
    '''
    print(colored("\n\nMetodo de Wald", 'magenta'))
    minx = []
    maxx = []
    for _, row in matrix.iterrows():
        array = np.array(row)
        minx.append(np.min(array))  # for benefits
        maxx.append(np.max(array))  # for costs
    maxy = np.argmax(minx)
    miny = np.argmin(maxx)

    # Results
    columns = name_rows(len(matrix.index))
    print(colored(
        f"\nProblema de Beneficios:\nSe recomienda elegir la alternativa {maxy}", 'cyan'))
    print(colored(f"Que presenta un coeficiente de {minx[maxy]}", 'cyan'))
    print(colored("Tabla de minimos", 'cyan'))
    utils.print_table([columns, minx])

    print(colored(
        f"\nProblema de Costos:\nSe recomienda elegir la alternativa {miny}", 'light_blue'))
    print(
        colored(f"Que presenta un coeficiente de {maxx[miny]}", 'light_blue'))
    print(colored("Tabla de maximos", 'light_blue'))
    utils.print_table([columns, maxx])

def analize_by_hurwicz(matrix, coef):
    '''
    Benefits ⇒ d(x) = α · maxy c(x, y) + (1 − α) · miny c(x, y)
    Costs ⇒ d(x) = α · miny c(x, y) + (1 − α) · max y c(x, y)
    '''
    print(colored("\n\nMetodo de Hurwicz", 'magenta'))
    complement = 1-coef
    benefits = []
    costs = []
    for _, row in matrix.iterrows():
        array = np.array(row)
        miny = np.min(array)
        maxy = np.max(array)
        benefits.append(coef*maxy + complement*miny)
        costs.append(coef*miny + complement*maxy)
    benefits = np.array(benefits)
    costs = np.array(costs)
    benefit = np.argmax(benefits)
    cost = np.argmin(costs)

    # Results
    columns = name_rows(len(matrix.index))
    print(colored(
        f"\nProblema de Beneficios:\nSe recomienda elegir la alternativa {benefit}", 'cyan'))
    print(
        colored(f"Que presenta un coeficiente de {benefits[benefit]}", 'cyan'))
    print(colored("Promedios ponderados", 'cyan'))
    utils.print_table([columns, benefits])

    print(colored(
        f"\nProblema de Costos:\nSe recomienda elegir la alternativa {cost}", 'light_blue'))
    print(
        colored(f"Que presenta un coeficiente de {costs[cost]}", 'light_blue'))
    print(colored("Promedios ponderados", 'light_blue'))
    utils.print_table([columns, costs])

def analize_by_savage(matrix, rows, columns):
    '''This method prints the suggested selected choice according with savage'''
    print(colored("\n\nMetodo de Savage", 'magenta'))
    benef_matrix, costs_matrix = generate_regret_matrixes(
        matrix, rows, columns)
    columns_name = name_columns(rows)

    # For benefits
    i, _, coef = wald_costs(benef_matrix)
    print(colored(
        f"\nProblema de Beneficios:\nSe recomienda elegir la alternativa {i}", 'cyan'))
    print(colored(f"Que presenta un coeficiente de {coef}", 'cyan'))
    print(colored("Matriz de arrepentimiento para beneficios", 'cyan'))
    utils.print_table(benef_matrix, columns_name)

    # For costs
    i, _, coef = wald_costs(costs_matrix)
    print(colored(
        f"\nProblema de Costos:\nSe recomienda elegir la alternativa {i}", 'light_blue'))
    print(colored(f"Que presenta un coeficiente de {coef}", 'light_blue'))
    print(colored("Matriz de arrepentimiento para costos", 'light_blue'))
    utils.print_table(costs_matrix, columns_name)

def wald_costs(matrix):
    ''' It returns the index of the minimax
    (the number of the suggested selected choice)
    along with the selected coeficient.
    '''
    maxx = []
    j_indexes = []
    for _, row in matrix.iterrows():
        array = np.array(row)
        maxx.append(np.max(array))
        j_indexes.append(np.argmax(array))
    miny = np.argmin(maxx)

    return miny, j_indexes[miny], maxx[miny]

def wald_benefits(matrix):
    ''' It returns the row index of the maximin
    (the number of the suggested selected choice), 
    the index of column of the election, 
    along with the selected coeficient.
    '''
    minx = []
    j_indexes = []
    for _, row in matrix.iterrows():
        array = np.array(row)
        minx.append(np.min(array))
        j_indexes.append(np.argmin(array))
    maxy = np.argmax(minx)
    
    return maxy, j_indexes[maxy], minx[maxy]

def generate_regret_matrixes(matrix, rows, columns):
    '''This method returns both regret matrixes, 
    one for benefits and another for costs, 
    given a [matrix] passed by parameter
    '''
    benef_regret = pd.DataFrame(columns=range(columns))
    costs_regret = pd.DataFrame(columns=range(columns))
    max_col = []
    min_col = []
    for column_name in matrix.columns:
        column_data = matrix[column_name]
        max_col.append(column_data.max())
        min_col.append(column_data.min())

    for i in range(rows):
        benef_row = []
        costs_row = []
        for j in range(columns):
            element = matrix.iloc[i, j]
            benef_row.append(max_col[j] - element)
            costs_row.append(element - min_col[j])
        benef_regret.loc[i] = benef_row
        costs_regret.loc[i] = costs_row

    return benef_regret, costs_regret

def name_columns(length):
    '''This method returns an array with the name of the nature statuses'''
    columns = []
    for i in range(length):
        columns.append(f'Estado {i}')

    return columns

def name_rows(length):
    '''This method returns an array with the name of choices'''
    columns = []
    for i in range(length):
        columns.append(f'Alternativa {i}')

    return columns
