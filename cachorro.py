from animal import Animal
class Cachorro(Animal): # cria a classe Gato derivada de Animal
    def __init__(self, nome, peso, posicao):
        super().__init__(nome, peso, posicao)
    
    def latir(self):
        print (f"Sou {self.nome}! Au-au...");