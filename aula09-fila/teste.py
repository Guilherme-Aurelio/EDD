from fila import Fila

fila = Fila()

print("A fila está vazia? ", fila.is_empty())

fila.put(10)
fila.put(20)
fila.put(30)

print("Tamanho da fila: ", fila.get_size())
fila.list_items()

print("Removendo o primeiro elemento: ", fila.remove()) 
print("Tamanho da fila: ", fila.get_size()) 
fila.list_items()

print("Primeiro elemento da fila: ", fila.get()) 