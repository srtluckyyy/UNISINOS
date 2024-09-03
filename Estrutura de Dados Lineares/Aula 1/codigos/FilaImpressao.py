class FilaImpressao:
    def __init__(self):
        self.fila = []

    def adicionar_tarefa(self, documento):
        """Adiciona um documento à fila de impressão"""
        self.fila.append(documento)

    def processar_fila(self):
        """Processa a fila de impressão removendo e imprimindo cada documento"""
        while self.fila:
            documento = self.fila.pop(0)
            print(f"Imprimindo: {documento}")

# Exemplo de uso da classe FilaImpressao
fila = FilaImpressao()
fila.adicionar_tarefa("Documento1.pdf")
fila.adicionar_tarefa("Documento2.pdf")
fila.adicionar_tarefa("Documento3.pdf")
fila.processar_fila()
