# -*- coding: utf-8 -*-
'''
    Um pequeno sapo quer chegar ao outro lado de uma estrada.
    Inicialmente o sapo está localizado na posição X e quer chegar a uma
    posição maior ou igual a Y. 
    O sapo sempre pula uma distancia fixa, D.

    Escreva uma função:

        def solution(X, Y, D):

    que, dados trẽs inteiros X, Y e D, retorna o número mínimo de pulos
    para ir da posição X para uma posição maior ou igual a Y.

    Por exemplos, dados:
        X = 10
        Y = 85
        D = 30

    a função deve retornar 3, pois o sapo se posicionará:
        depois do primeiro pulo, na posição 10 + 30 = 40
        depois do segundo pulo, na posição 40 + 30 = 70
        depois do terceiro pulo, na posição 70 + 30 = 100 > 85

    Escreva um algorítmo --eficiente-- dadas as seguintes condições:
        X, Y e D são inteiros no intervalo [1, 1.000.000.000]
        X <= Y
'''

def solution(X, Y, D):
    return

inputs = [
    [10, 85, 30]
]

expecteds = [3]


for i in range(len(inputs)):
    result = solution(inputs[i][0], inputs[i][1], inputs[i][2])
    expected = expecteds[i]
    if result == expected:
        print('OK')
    else:
        print('Error while testing for %s. Expected %s, but got %s' %
              (inputs[i], result, expected))