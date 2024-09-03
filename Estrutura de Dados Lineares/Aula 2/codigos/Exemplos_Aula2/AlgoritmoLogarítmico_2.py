# Nome do arquivo: exemplo_pesquisa_binaria.py
import time  # Importa o módulo time para poder medir o tempo de execução do código

# Função que implementa o algoritmo de pesquisa binária em uma lista ordenada.
# Este método demonstra uma complexidade de tempo O(log n), pois divide o espaço de busca pela metade em cada etapa.
def pesquisa_binaria(lista, alvo):
    # Inicializa os índices que delimitam a parte da lista a ser pesquisada
    inferior, superior = 0, len(lista) - 1
    
    # Continua a busca enquanto o intervalo não for esgotado
    while inferior <= superior:
        # Calcula o índice do meio do intervalo
        meio = (inferior + superior) // 2 # Divisão inteira (//) para garantir que o resultado seja um inteiro.
        
        # Verifica se o elemento no meio da lista é o alvo
        if lista[meio] == alvo:
            return meio  # Retorna o índice do elemento encontrado
        elif lista[meio] > alvo:
            superior = meio - 1  # Ajusta o índice superior para descartar a metade superior da lista
        else:
            inferior = meio + 1  # Ajusta o índice inferior para descartar a metade inferior da lista
    
    return -1  # Retorna -1 caso o alvo não seja encontrado na lista

# Medição do tempo de execução do algoritmo.
tempo_inicio = time.time()  # Guarda o tempo no momento inicial da execução
resultado = pesquisa_binaria([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)  # Executa a pesquisa binária, O número 5 é escolhido como o valor de alvo ("target")
tempo_fim = time.time()  # Guarda o tempo no momento final da execução

# Exibe o resultado da busca e o tempo de execução
print("Resultado:", resultado)  # Imprime o índice do elemento encontrado
print("Tempo de execução (O(log n)):", tempo_fim - tempo_inicio, "segundos")  # Calcula e imprime o tempo gasto na execução

"""
                        [1, 2, 3, 4, 5, 6, 7, 8, 9]
                                  /       \
                   [1, 2, 3, 4]              [5, 6, 7, 8, 9]
                     /     \                    /       \
                [1, 2]      [3, 4]           [5, 6]     [7, 8, 9]
                  /   \      /   \            /   \       /   \
               [1]  [2]   [3]   [4]         [5]  [6]    [7]  [8, 9]
                                              ...
                                            (encontra 4)

"""
