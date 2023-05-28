'''Juego de suma cero entre dos jugadores que quieren ganarle al otro.
Se busca un punto de silla o de equilibrio en el que los dos queden contentos.
Tiene que poder determinar cuando no se puede resolver por estrategia pura.
El jugador se utilizará el criterio maximin, el oponente se utilizará el criterio minimax.'''

import uncertain_universe
from termcolor import colored


def decide(matrix):
    '''It says whether the game can be solved with a pure strategy or not.
    Also if it is the case of a pure strategy it prints the sadle point.'''
    row_player1, col_player1, coef_player1 = uncertain_universe.wald_benefits(
        matrix)
    col_player2, row_player2, coef_player2 = uncertain_universe.wald_costs(
        matrix.transpose())
    print(
        f'El jugador 1 toma la estrategia: ({row_player1}, {col_player1}), de valor: {coef_player1}')
    print(
        f'El jugador 2 toma la estrategia: ({row_player2}, {col_player2}), de valor: {coef_player2}')
    if (row_player1 == row_player2) & (col_player1 == col_player2):
        print(
            colored('El juego de suma cero se puede resolver por estrategia pura', 'green'))
        print(
            colored(f'El punto silla es = {row_player1, col_player1}', 'green'))
        print(colored(f'El valor de juego es {coef_player1}', 'green'))
    else:
        print(colored(
            "El juego de suma cero no ha podido ser resulto mediante una estrategia pura.", "red"))
