import os
from search import Search

def main(question: str, array: list, value: int): # Função para evitar repetição de código
    def __searching(search_type: str, search_list: list): 
        if len(search_list) > 1:
            print(f"Valor encontrado na posição {search_list[0]}, com {search_list[1]} passos\n")
        else:
            print(f"Valor NÃO encontrado. Passos realizados pela pesquisa {search_type}: {search_list[0]}")

    search = Search()

    print(f"\n\n\nQuestão {question}:")
    print(f"Pesquisando o valor {value}")

    # Pesquisa sequencial
    sequencial = search.sequencial_search(array, value)
    __searching("sequencial", sequencial)

    # Pesquisa binária
    binary = search.binary_search(array, value)
    __searching("binária", binary)

    input("Pressione ENTER para continuar...")

# Questões:
#1. Mostre (indique a ordem em que as posições são percorridas no próprio array) os
# passos realizados pela pesquisa sequencial e pela pesquisa binária no array
# abaixo para encontrar o valor 87.
# [2, 5, 9, 12, 15, 20, 22, 26, 30, 45, 87, 92, 100]

os.system('cls' if os.name == 'nt' else 'clear')
arrayQ1 = [2, 5, 9, 12, 15, 20, 22, 26, 30, 45, 87, 92, 100]
main("1", arrayQ1, 87)

#2. Mostre (indique a ordem em que as posições são percorridas no próprio array) os
# passos realizados pela pesquisa binária no array abaixo para encontrar o valor 21.
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

#os.system('cls' if os.name == 'nt' else 'clear')
arrayQ2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
main("2", arrayQ2, 21)

#3. Nos arrays abaixo, mostre os passos realizados pelo algoritmo de pesquisa binária
# para encontrar o elemento 18. Caso não seja possível aplicar a pesquisa binária, explique o motivo. 
# [3, 12, 24, 76, 45, 27, 9, 18, 32, 11, 20, 19, 88, 101]
# [-4, 2, 7, 18, 28, 29, 56, 77, 81, 84, 92, 100, 112, 132]

#Abrahao note: utilizar a pesquisa binaria não foi só possivel, como foi ate melhor que a sequencial.

arrayQ3_1 = [3, 12, 24, 76, 45, 27, 9, 18, 32, 11, 20, 19, 88, 101]
arrayQ3_2 = [-4, 2, 7, 18, 28, 29, 56, 77, 81, 84, 92, 100, 112, 132]

main("3 - 1° array", arrayQ3_1, 18)
main("3 - 2° array", arrayQ3_2, 18)
