'''
Classe Pais:
◦ Classe que representa um país.
◦ Um país possui um código ISO 3166-1 (ex.: BRA), um nome (ex.: Brasil), uma população (ex.: 193.946.886) e uma dimensão em Km2 
(ex.: 8.515.767,049). Além disso, um país mantém uma lista de outros países com os quais ele faz fronteira.
◦ Crie um construtor que inicialize o código ISO, o nome e a dimensão do país.
◦ Crie os métodos de acesso e modificadores (getter/setter) para os atributos código ISO, nome, população e dimensão.
◦ Crie um método que permita verificar se dois objetos representam o mesmo país (igualdade semântica). 
Dois países são iguais se tiverem o mesmo código ISO.
◦ Crie um método que informe se outro país é limítrofe do país que recebeu a mensagem.
◦ Crie um método que retorne a densidade populacional do país.
◦ Crie um método que receba um país como parâmetro e retorne a lista de vizinhos comuns aos dois países. 
Considere que um país tem no máximo 40 outros países com os quais ele faz fronteira.
'''



class Pais:
    def __init__(self, ISO: str, nome: str, populacao_Mi: float, dimensao_Mi_KM2: float) -> None:
        self.__name = nome
        self.__ISO = ISO
        self.__population = populacao_Mi
        self.__dimension = dimensao_Mi_KM2


    @property
    def nome(self):
        return self.__name
    

    @property
    def iso(self):
        return self.__ISO
    

    @property
    def populacao(self):
        return self.__population
    

    @property
    def dimensao(self):
        return self.__dimension
    

    @nome.setter
    def nome(self, nome):
        self.__name = nome
    

    @iso.setter
    def iso(self, iso):
        self.__ISO = iso
    

    @populacao.setter
    def populacao (self, pop):
        self.__population = pop


    @dimensao.setter
    def dimensao(self, dimension):
        self.__dimension = dimension


    #Crie um método que permita verificar se dois objetos representam o mesmo país (igualdade semântica). 
    #Dois países são iguais se tiverem o mesmo código ISO.
    def __eq__(self, pais: object) -> bool:
        if self == pais: return True
        elif self.__ISO == pais.__iso: return True
        else: return False


    #Crie um método que informe se outro país é limítrofe do país que recebeu a mensagem.
    def isNeigh(self):
        pass

    
    #Crie um método que retorne a densidade populacional do país.
    def popuDensity(self):
        pass


    #Crie um método que receba um país como parâmetro e retorne a lista de vizinhos comuns aos dois países.
    def neighinCommon(self):
        pass


    def imprimi_info(self):
        pass
