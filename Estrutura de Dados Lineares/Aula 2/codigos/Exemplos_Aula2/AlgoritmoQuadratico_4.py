import time  # Importa o módulo time para medir o tempo de execução

# Função para gerar uma matriz de produtos de todos os pares de elementos.
# Este exemplo demonstra uma complexidade O(n^2) devido aos dois loops aninhados (nested loops).
def gerar_matriz_de_produtos(elementos):
    matriz = []  # Inicializa uma lista vazia para armazenar a matriz de produtos
    for i in elementos:  # Primeiro loop: percorre cada elemento da lista
        linha = []  # Inicializa uma lista vazia para armazenar a linha de produtos
        for j in elementos:  # Segundo loop: percorre cada elemento da lista novamente
            linha.append(i * j)  # Multiplica o elemento 'i' pelo elemento 'j' e adiciona o resultado à linha
        matriz.append(linha)  # Adiciona a linha de produtos à matriz
    return matriz  # Retorna a matriz completa de produtos

# Medindo o tempo de execução da função.
inicio = time.time()  # Marca o tempo inicial antes de executar a função
resultado = gerar_matriz_de_produtos([1, 2, 3])  # Chama a função com uma lista de três elementos
fim = time.time()  # Marca o tempo final após a execução da função

# Exibe o resultado e o tempo de execução.
print("Resultado:", resultado)  # Exibe a matriz de produtos
print("Tempo de execução (O(n^2)):", fim - inicio, "segundos")  # Exibe o tempo total de execução
