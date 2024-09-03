import time  # Importa o módulo de tempo para medir a execução do programa
import random  # Importa o módulo random para gerar números aleatórios

def somar_elementos(elementos):
    total = 0  # Inicia a variável total em 0 para acumular a soma dos elementos
    for elemento in elementos:  # Itera sobre cada elemento na lista fornecida
        total += elemento  # Adiciona o valor do elemento ao total
    return total  # Retorna o valor total acumulado

# Função para formatar o número com pontuação e retornar a escala (mil, milhão, bilhão, etc.)
def formatar_numero_e_escala(valor):
    if valor < 1_000:
        return f"{valor:,}", "unidades"
    elif valor < 1_000_000:
        return f"{valor:,}", "milhares"
    elif valor < 1_000_000_000:
        return f"{valor:,}", "milhões"
    elif valor < 1_000_000_000_000:
        return f"{valor:,}", "bilhões"
    else:
        return f"{valor:,}", "trilhões"

tamanho_da_lista = 10**7  # Define o tamanho inicial da lista
lista_aleatoria = [random.randint(1, 100) for _ in range(tamanho_da_lista)]  # Gera a lista com números aleatórios

inicio = time.time()  # Marca o tempo inicial
resultado = somar_elementos(lista_aleatoria)  # Calcula a soma dos elementos da lista
fim = time.time()  # Marca o tempo final

tempo_de_execucao = fim - inicio  # Calcula o tempo de execução

resultado_formatado, escala = formatar_numero_e_escala(resultado)  # Formata o resultado e obtém a escala

print(f"Resultado da soma: {resultado_formatado} ({escala})")  # Exibe o resultado formatado e a escala
print(f"Tempo de execução (O(n)): {tempo_de_execucao:.2f} segundos")  # Exibe o tempo de execução formatado com duas casas decimais

contador_dobras = 0  # Inicia o contador de dobras

if tempo_de_execucao < 3:
    print("Ajustando o tamanho da lista para aumentar o tempo de execução...")
    while tempo_de_execucao < 3:  # Enquanto o tempo de execução for menor que 3 segundos, continua ajustando
        tamanho_da_lista *= 2  # Dobra o tamanho da lista
        lista_aleatoria = [random.randint(1, 100) for _ in range(tamanho_da_lista)]  # Gera nova lista
        inicio = time.time()  # Marca o tempo inicial novamente
        resultado = somar_elementos(lista_aleatoria)  # Recalcula a soma com a nova lista
        fim = time.time()  # Marca o tempo final novamente
        tempo_de_execucao = fim - inicio  # Recalcula o tempo de execução
        contador_dobras += 1  # Incrementa o contador de dobras

    resultado_formatado, escala = formatar_numero_e_escala(resultado)  # Formata o novo resultado
    print(f"Foi necessário dobrar o tamanho da lista {contador_dobras} vezes.")
    print(f"Resultado final da soma: {resultado_formatado} ({escala})")
    print(f"Tempo de execução final (O(n)): {tempo_de_execucao:.2f} segundos")
else:
    print("Não foi necessário dobrar o tamanho da lista para atingir três segundos.")
