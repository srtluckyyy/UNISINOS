'''
Classe Continente:
◦ Um continente possui um nome e é composto por um conjunto de países.
◦ Crie um construtor que inicialize o nome do continente.
◦ Crie um método que permita adicionar países aos continentes.
◦ Crie um método que retorne a dimensão total do continente.
◦ Crie um método que retorne a população total do continente.
◦ Crie um método que retorne a densidade populacional do continente.
◦ Crie um método que retorne o país com maior população no continente.
◦ Crie um método que retorne o país com menor população no continente.
◦ Crie um método que retorne o país de maior dimensão territorial no continente.
◦ Crie um método que retorne o país de menor dimensão territorial no continente.
◦ Crie um método que retorne a razão territorial do maior país em relação ao menor país.
'''
from pais import Pais



class Continente:
    def __init__(self, nome: str) -> None:
        self.__name = nome


    @property
    def nome(self):
        return self.__name
    

    @nome.setter
    def nome(self, nome):
        self.__name = nome
  
    
    def addCountry(self, pais: Pais):
        pass


    def totalDimension(self) -> float:
        pass


    def totalPop(self) -> float:
        pass


    def popDensity(self) -> float:
        pass


    def maxPopinCountry(self):
        pass


    def minPopinCountry(self):
        pass


    def ratioTerritoryCountryvsCountry(self) -> float:
        pass

    
    def imprimi_info(self):
        pass
