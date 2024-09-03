import time  # Importa o módulo time para medir o tempo de execução

# Função recursiva para calcular o n-ésimo número de Fibonacci
def fibonacci(n):
    # Base da recursão: os primeiros dois números de Fibonacci são 0 e 1.
    if n <= 1:
        return n  # Retorna 'n' se for 0 ou 1, que são os primeiros números da sequência de Fibonacci
    # Chamada recursiva que segue a definição de Fibonacci: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # Soma os resultados das duas chamadas recursivas

# Medindo o tempo de execução.
tempo_inicial = time.time()  # Marca o tempo inicial antes de calcular o número de Fibonacci
resultado = fibonacci(10)  # Calcula o 10º número da sequência de Fibonacci
tempo_final = time.time()  # Marca o tempo final após a execução

# Exibe o resultado e o tempo de execução
print("Resultado:", resultado)  # Exibe o resultado, ou seja, o 10º número de Fibonacci
print("Tempo de execução (O(2^n)):", tempo_final - tempo_inicial, "segundos")  # Exibe o tempo total de execução


