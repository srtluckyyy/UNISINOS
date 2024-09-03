
### REVISAR com o Professor ###

'''
Calcule a função T(n) para o algoritmo abaixo
assumindo que é uma matriz quadrada. Apresente
também a classe de complexidade.
'''
import numpy as np

def somar(a: np.matrix) -> int:
    somar: int = 0
    for i, _ in enumerate(a):
        for j, _ in enumerate(a[i]): 
            somar += a[i][j] 
    return somar 

# T(n) = 2n² + 2n + 3
#   Classe = O(n2)
