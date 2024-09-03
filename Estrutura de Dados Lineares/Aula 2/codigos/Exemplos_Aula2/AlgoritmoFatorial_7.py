import time  # Importa o módulo time para medir o tempo de execução
from itertools import permutations  # Importa a função permutations da biblioteca itertools

# Função para gerar todas as permutações de uma lista.
def todas_permutacoes(elementos):
    # O itertools.permutations gera todas as permutações possíveis da lista fornecida.
    return list(permutations(elementos))  # Converte o resultado do permutations em uma lista

# Medindo o tempo de execução da função de permutações.
tempo_inicial = time.time()  # Marca o tempo inicial antes de calcular as permutações
resultado = todas_permutacoes([1, 2, 3, 4])  # Gera todas as permutações de uma lista com 4 elementos
tempo_final = time.time()  # Marca o tempo final após a execução da função

# Exibe o número de permutações geradas e o tempo de execução
print("Resultado:", len(resultado), "permutações")  # Exibe o número total de permutações geradas
print("Tempo de execução (O(n!)):", tempo_final - tempo_inicial, "segundos")  # Exibe o tempo de execução em segundos
