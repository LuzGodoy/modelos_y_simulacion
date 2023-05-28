'''File of common utils that can be used everywhere along the proyect'''
from tabulate import tabulate as tab

def print_table(matrix, headers=None):
    '''This is a method to unify the printing of a table with a rounded style.'''
    if headers is None :
        table=tab(
            matrix,
            tablefmt='rounded_grid',
            stralign='center',
            floatfmt=".2f"
        )
    else:
        table=tab(
            matrix,
            tablefmt='rounded_grid',
            stralign='center',
            floatfmt=".2f",
            headers=headers
        )
    print(table)
