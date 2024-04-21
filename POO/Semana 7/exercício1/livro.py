class Livro: 
    def __init__(self, titulo: str) -> None:
        self.titulo = titulo
        self.exemplares = 0
        self.emprestados = 0

    
    def verifica_dispo(self, qnt_requeridos) -> bool:
        disponibilidade = self.exemplares - self.emprestados

        if disponibilidade >= qnt_requeridos: return True
        if disponibilidade < qnt_requeridos: return False
