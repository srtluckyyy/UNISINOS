'''
📋 Objetivos:
    Entender como funcionam as pesquisas sequencial e binária.
    Implementar e testar os algoritmos em Python.
    Analisar as vantagens e desvantagens de cada método de pesquisa.

💻 Instruções:
    Copie o código fornecido abaixo e cole no seu editor Python.
    Execute o código e observe a saída no console. Teste a pesquisa sequencial, a pesquisa binária, e a pesquisa mista.
    Responda às perguntas no final da atividade para refletir sobre o desempenho e a aplicabilidade dos métodos de pesquisa.

Perguntas para Reflexão:
    1. Qual foi a posição do livro "Harry Potter" na lista original usando pesquisa sequencial?
        Na posição 5.
    
    2. Como a posição do livro mudou ao utilizar a pesquisa binária? Por quê?
        Porque foi utilizado a função sort() para ordenar a lista antes de realizar a pesquisa binária. Ai a lista mudou para:
        > ['1984', 'A Guerra dos Tronos', 'Cem Anos de Solidão', 'Dom Quixote', 'Harry Potter', ...]
        Colocando o livro "Harry Potter" na posição 4 do array.
     
    3. Em qual situação você acha que a pesquisa sequencial seria mais útil do que a pesquisa binária?
        Quando a lista é pequena, a pesquisa sequencial é mais eficiente.

    4. Explique como a pesquisa mista decide qual método utilizar. Quando você acha que essa abordagem é mais vantajosa?
        A pesquisa mista decide qual método utilizar baseado no tamanho da lista comparando-a com o limite, que por padrão é 5. Se a  lista for pequena, será feita a sequencial, caso contrario será a binária.
        Acho que só quando não se tem certeza de qual vai ser o tamanho da lista, ou quando vai ser verificado várias listas de tamanhos diferentes.
'''


# Lista de títulos de livros (desordenada)
livros = [
    "O Senhor dos Anéis", "1984", "Dom Quixote", 
    "O Pequeno Príncipe", "A Guerra dos Tronos", 
    "Harry Potter", "Moby Dick", "Orgulho e Preconceito",
    "O Alquimista", "O Código Da Vinci", "Cem Anos de Solidão"
]

# Função de Pesquisa Sequencial
def pesquisa_sequencial(lista, valor_procurado):
    print("\nRealizando Pesquisa Sequencial...")
    for i, item in enumerate(lista):
        if item == valor_procurado:
            return i
    return -1

# Função de Pesquisa Binária (a lista precisa estar ordenada)
def pesquisa_binaria(lista, valor_procurado):
    print("\nRealizando Pesquisa Binária...")
    esquerda = 0
    direita = len(lista) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == valor_procurado:
            return meio
        elif lista[meio] < valor_procurado:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

# Função para combinar Pesquisa Sequencial e Binária
def pesquisa_mista(lista, valor_procurado, limite_sequencial=5):
    if len(lista) <= limite_sequencial:
        # Para listas pequenas, usa Pesquisa Sequencial
        return pesquisa_sequencial(lista, valor_procurado)
    else:
        # Para listas maiores, usa Pesquisa Binária após ordenar
        lista.sort()  # Ordena a lista antes da pesquisa binária
        return pesquisa_binaria(lista, valor_procurado)

# Bloco principal de execução
if __name__ == "__main__":
    # Exibir a lista original
    print("Lista original de livros:")
    for livro in livros:
        print(livro)
    
    # Título do livro a ser pesquisado
    titulo_procurado = "Harry Potter"
    
    # Teste com Pesquisa Sequencial
    posicao = pesquisa_sequencial(livros, titulo_procurado)
    if posicao != -1:
        print(f"\nTítulo '{titulo_procurado}' encontrado na posição: {posicao} (Pesquisa Sequencial)")
    else:
        print(f"\nTítulo '{titulo_procurado}' não encontrado na lista. (Pesquisa Sequencial)")

    # Teste com Pesquisa Binária (requer lista ordenada)
    # Ordenando a lista antes de fazer a pesquisa binária
    livros_ordenados = sorted(livros)
    posicao = pesquisa_binaria(livros_ordenados, titulo_procurado)
    if posicao != -1:
        print(f"\nTítulo '{titulo_procurado}' encontrado na posição: {posicao} (Pesquisa Binária)")
    else:
        print(f"\nTítulo '{titulo_procurado}' não encontrado na lista. (Pesquisa Binária)")

    # Teste com Pesquisa Mista
    posicao = pesquisa_mista(livros, titulo_procurado)
    if posicao != -1:
        print(f"\nTítulo '{titulo_procurado}' encontrado na posição: {posicao} (Pesquisa Mista)")
    else:
        print(f"\nTítulo '{titulo_procurado}' não encontrado na lista. (Pesquisa Mista)")
