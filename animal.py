class Animal:
    def __init__(self, nome, peso, posicao):
        self.__nome = nome
        self.__peso = peso
        self.__posicao = posicao
    
    @property
    def nome (self):
        return self.__nome
    
    @property
    def peso (self):
        return self.__peso
    
    @peso.setter
    def peso (self, peso):
        self.__peso = peso
    
    @property
    def posicao (self):
        return self.__posicao
    
    @posicao.setter
    def posicao(self, pos):
        self.__posicao = pos
    
    def moverse(self):
        self.__posicao += 1
