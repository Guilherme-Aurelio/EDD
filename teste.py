from cachorro import Cachorro
from gato import Gato

gato = Gato("Bonitão", 7, 0)
cachorro = Cachorro("Max", 40, 0)
gato.miar()
cachorro.latir()

gato.moverse()
gato.moverse()
gato.moverse()
gato.moverse()
gato.moverse()

cachorro.moverse()
cachorro.moverse()
cachorro.moverse()

print("Posição do gato: ", gato.posicao)
print("Posição do cachorro: ", cachorro.posicao)