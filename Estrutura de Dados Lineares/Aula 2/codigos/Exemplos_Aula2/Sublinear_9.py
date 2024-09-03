import time  # Importa o módulo time para medir o tempo de execução
import math  # Importa o módulo math para usar a função sqrt (raiz quadrada)

# Função para processar elementos até a raiz quadrada do tamanho total da lista.
def processo_raiz_quadrada(elementos):
    resultado = 0  # Inicializa o resultado com 0
    # Processa apenas até a raiz quadrada do número de elementos.
    for i in range(int(math.sqrt(len(elementos)))):  # Itera apenas até a raiz quadrada do comprimento da lista
        resultado += elementos[i]  # Soma o valor do elemento atual ao resultado
    return resultado  # Retorna o valor acumulado

# Medindo o tempo de execução da função.
tempo_inicial = time.time()  # Marca o tempo inicial antes da execução
resultado = processo_raiz_quadrada(list(range(10000)))  # Chama a função com uma lista de 10000 elementos
tempo_final = time.time()  # Marca o tempo final após a execução

# Exibe o resultado e o tempo de execução.
print("Resultado:", resultado)  # Exibe o resultado da soma parcial
print("Tempo de execução (O(√n)):", tempo_final - tempo_inicial, "segundos")  # Exibe o tempo total de execução
