import time  # Importa o módulo time para medir o tempo de execução
import math  # Importa o módulo math para utilizar funções matemáticas, como logaritmo

# Função exemplificativa para um processo que requer decisões logarítmicas múltiplas.
def processo_decisao_complexa(n):
    resultado = 0  # Inicializa a variável resultado com 0 para acumular as somas
    # Loop aninhado que executa operações baseadas no logaritmo ao quadrado.
    for i in range(int(math.log(n, 2)) + 1):  # O loop externo vai até o valor do logaritmo de n na base 2, somando 1
        for j in range(int(math.log(n, 2)) + 1):  # O loop interno faz o mesmo, criando um aninhamento logarítmico
            resultado += i * j  # Multiplica i por j e acumula o resultado
    return resultado  # Retorna o valor final acumulado

# Medindo o tempo de execução da função.
tempo_inicial = time.time()  # Marca o tempo inicial antes da execução do processo
resultado = processo_decisao_complexa(1024)  # Chama o processo com uma entrada de tamanho 1024
tempo_final = time.time()  # Marca o tempo final após a execução

# Exibe o resultado e o tempo de execução.
print("Resultado:", resultado)  # Exibe o resultado acumulado do processo
print("Tempo de execução (O(log(n)^2)):", tempo_final - tempo_inicial, "segundos")  # Exibe o tempo total de execução
