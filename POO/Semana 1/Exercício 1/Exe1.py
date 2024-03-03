'''
1. Crie uma matriz com dimensão 4 linhas por 6 colunas e peça para o usuário informar
somente os valores da primeira linha, todos eles números inteiros. Em seguida, realize
as seguintes ações:

        a) A segunda linha deve ser uma cópia da primeira, em ordem inversa das colunas.

        b) A terceira linha deve ser a soma dos elementos da primeira e segunda linhas,
    coluna por coluna, respeitando suas respectivas posições.

        c) A quarta linha deve conter os números pares da primeira linha seguidos dos
    números ímpares também da primeira linha, um por coluna.

        d) Imprima a matriz normal e a transposta, utilizando o caractere “tab” como
    separador das colunas.
'''

def cMatriz(colunas = 6, linhas = 4):
    matriz = [[0 for c in range(colunas)] for l in range(linhas)]
    print(matriz)
    return matriz

def primeriaLinha(matriz: list, colunas = 6):
    matriz[0].clear()
    for i in range(colunas):
        n = int(input(f'Digite o {i + 1}o número: '))
        matriz[0].insert(i, n)
        print(matriz)

def constrMatriz(matriz: list, colunas = 6, linhas = 4):
    for i in range(colunas):
        matriz[1].append(matriz[i + 1 + ])
    pass

def main():
    coluna = 6
    linha = 4

    matriz = cMatriz(coluna, linha)
    primeriaLinha(matriz, coluna)
    constrMatriz(matriz, coluna, linha)

main()
