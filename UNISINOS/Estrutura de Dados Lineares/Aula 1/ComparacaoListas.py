import time

class ComparacaoListas:
    def __init__(self):
        self.array_list = []
        self.linked_list = []

    def adicionar_array_list(self, n):
        """Adiciona elementos em um array_list e mede o tempo de inserção"""
        tempo_inicio = time.time_ns()
        for i in range(n):
            self.array_list.append(i)
        tempo_fim = time.time_ns()
        print(f"Tempo de inserção no ArrayList: {tempo_fim - tempo_inicio} ns")

    def adicionar_linked_list(self, n):
        """Adiciona elementos em uma linked_list e mede o tempo de inserção"""
        tempo_inicio = time.time_ns()
        for i in range(n):
            self.linked_list.append(i)
        tempo_fim = time.time_ns()
        print(f"Tempo de inserção no LinkedList: {tempo_fim - tempo_inicio} ns")

# Exemplo de uso da classe ComparacaoListas
comparacao = ComparacaoListas()
comparacao.adicionar_array_list(100000)
comparacao.adicionar_linked_list(100000)
