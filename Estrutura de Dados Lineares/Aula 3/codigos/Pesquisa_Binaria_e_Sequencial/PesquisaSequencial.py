# Exemplo de Pesquisa Sequencial
def pesquisa_sequencial(lista, valor_procurado):
    print("Lista: ", lista)  # Exibindo a lista para facilitar o entendimento
    print(f"Procurando o valor {valor_procurado}...\n")
    
    # Percorrendo cada elemento da lista
    for i, elemento in enumerate(lista):
        print(f"Passo {i+1}: Verificando o elemento {elemento}")
        
        # Se o valor for encontrado, retorna o índice
        if elemento == valor_procurado:
            print(f"Encontrado! {valor_procurado} está na posição {i}.\n")
            return i
        
        # Se não for encontrado, continuar verificando
        else:
            print(f"{elemento} não é o valor procurado...\n")
    
    # Se chegar ao final sem encontrar, retornar -1
    print(f"O valor {valor_procurado} não está na lista.\n")
    return -1

# Exemplo de uso
lista_exemplo = [5, 8, 12, 20, 33]
pesquisa_sequencial(lista_exemplo, 12)
