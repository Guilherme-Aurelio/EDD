from animal import Animal
class Gato(Animal): # cria a classe Gato derivada de Animal
    def __init__(self, nome, peso, posicao):
        super().__init__(nome, peso, posicao)
    
    def miar(self):
        print (f"Sou {self.nome}! Miauu")