'''
Calcule a função T(n) para o algoritmo abaixo
assumindo que é uma matriz quadrada. Apresente
também a classe de complexidade.
'''

import numpy as np

def imprimir(a: np.matrix) -> None:
    i: int = 0                          # 1
    while i < len(a):                   # n + 1
        j: int = 0                      # n
        while j < len(a[i]):            # n . (n + 1) => n2 + n
            print(a[i][j], end=' ')     # n . n => n2
            j +=1                       # n . n => n2
        print()                         # n
        i +=1                           # n
        
# T(n) = 3n2 + 5n + 2
#    Classe = O(n2)
