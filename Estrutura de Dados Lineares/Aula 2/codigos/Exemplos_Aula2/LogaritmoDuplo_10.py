import time  # Importa o módulo time para medir o tempo de execução
import math  # Importa o módulo math para utilizar funções matemáticas, como logaritmo

# Função para executar um processo que cresce com o logaritmo do logaritmo do tamanho da entrada.
def processo_logaritmo_duplo(n):
    resultado = 0  # Inicializa o resultado como 0
    # Loop que depende do logaritmo do logaritmo do valor de entrada.
    for i in range(int(math.log(math.log(n, 2), 2)) + 1):  # Calcula log(log(n)) na base 2
        resultado += i  # Acumula o valor de i no resultado
    return resultado  # Retorna o valor acumulado

# Medindo o tempo de execução da função.
tempo_inicial = time.time()  # Marca o tempo inicial antes da execução
resultado = processo_logaritmo_duplo(65536)  # Chama a função com uma entrada de tamanho 65536
tempo_final = time.time()  # Marca o tempo final após a execução

# Exibe o resultado e o tempo de execução.
print("Resultado:", resultado)  # Exibe o resultado acumulado
print("Tempo de execução (O(log log(n))):", tempo_final - tempo_inicial, "segundos")  # Exibe o tempo total de execução
