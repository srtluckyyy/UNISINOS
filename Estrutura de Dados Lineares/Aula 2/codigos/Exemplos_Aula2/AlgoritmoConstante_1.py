# Nome do arquivo: exemplo_tempo_constante.py
import time  # Importação do módulo de tempo para medir a execução

# Esta função retorna o primeiro elemento de uma lista,
# demonstrando uma operação de tempo constante O(1).
def obter_primeiro_elemento(elementos):
    # Acesso direto ao primeiro elemento, que é uma operação constante.
    # Não importa o tamanho da lista, essa operação sempre levará o mesmo tempo.
    return elementos[0]

# Medindo o tempo de execução.
inicio = time.time()  # Guarda o momento inicial antes da execução da função
resultado = obter_primeiro_elemento([1, 2, 3, 4, 5])  # Executa a função com uma lista de 5 elementos
fim = time.time()  # Guarda o momento final após a execução da função

# Exibe o resultado obtido e o tempo que levou para executar a função
print("Resultado:", resultado)
print("Tempo de execução (O(1)):", fim - inicio, "segundos")

