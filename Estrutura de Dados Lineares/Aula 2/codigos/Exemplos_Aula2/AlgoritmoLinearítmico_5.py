import time  # Importa o módulo time para medir o tempo de execução

# Implementação do Merge Sort (Ordenação por Fusão), que é um exemplo clássico de algoritmo O(n log n).
# O Merge Sort divide a lista em duas metades, ordena cada uma separadamente e depois as funde.
def ordenacao_fusao(lista):
    if len(lista) > 1:  # Verifica se o tamanho da lista é maior que 1
        meio = len(lista) // 2  # Encontra o ponto médio da lista
        esquerda = lista[:meio]  # Divide a lista na metade esquerda
        direita = lista[meio:]  # Divide a lista na metade direita

        # Chama recursivamente o ordenacao_fusao para ordenar cada metade
        ordenacao_fusao(esquerda)  # Ordena a metade esquerda
        ordenacao_fusao(direita)  # Ordena a metade direita

        # Inicializa os índices para fusão das duas metades
        i = j = k = 0

        # Funde as duas metades (esquerda e direita) em uma única lista ordenada
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:  # Compara os elementos de cada metade
                lista[k] = esquerda[i]  # Se o elemento da esquerda for menor, ele vai para lista[k]
                i += 1  # Incrementa o índice da esquerda
            else:
                lista[k] = direita[j]  # Se o elemento da direita for menor, ele vai para lista[k]
                j += 1  # Incrementa o índice da direita
            k += 1  # Move para a próxima posição de lista

        # Se ainda restarem elementos na metade esquerda, adiciona-os no final de lista
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        # Se ainda restarem elementos na metade direita, adiciona-os no final de lista
        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

# Medindo o tempo de execução da função de ordenação por fusão
lista = [38, 27, 43, 3, 9, 82, 10]  # Exemplo de uma lista não ordenada
tempo_inicial = time.time()  # Marca o tempo inicial antes de começar a ordenação
ordenacao_fusao(lista)  # Chama a função ordenacao_fusao para ordenar a lista
tempo_final = time.time()  # Marca o tempo final após a ordenação

# Exibe o resultado da lista ordenada e o tempo total de execução
print("Resultado:", lista)  # Exibe a lista ordenada após o Merge Sort
print("Tempo de execução (O(n log n)):", tempo_final - tempo_inicial, "segundos")  # Exibe o tempo de execução
