# Exemplo de Pesquisa Binária 
def pesquisa_binaria(lista, valor_procurado):
    print("Lista ordenada: ", lista)  # Exibindo a lista
    print(f"Procurando o valor {valor_procurado}...\n")
    
    # Inicializando os limites da busca
    esquerda = 0
    direita = len(lista) - 1
    
    passo = 1
    while esquerda <= direita:
        # Encontrando o ponto médio
        meio = (esquerda + direita) // 2
        print(f"Passo {passo}: Verificando o elemento do meio {lista[meio]} (posição {meio})")
        
        # Se encontrou o valor
        if lista[meio] == valor_procurado:
            print(f"Encontrado! {valor_procurado} está na posição {meio}.\n")
            return meio
        
        # Se o valor procurado é menor, busca na metade esquerda
        elif valor_procurado < lista[meio]:
            print(f"{valor_procurado} é menor que {lista[meio]}. Buscando na metade esquerda...\n")
            direita = meio - 1
        
        # Se o valor procurado é maior, busca na metade direita
        else:
            print(f"{valor_procurado} é maior que {lista[meio]}. Buscando na metade direita...\n")
            esquerda = meio + 1
        
        passo += 1
    
    # Se não encontrar o valor
    print(f"O valor {valor_procurado} não está na lista.\n")
    return -1

# Exemplo de uso - array ordenado
lista_exemplo = [2, 7, 15, 30, 40, 50, 90]
pesquisa_binaria(lista_exemplo, 90)
