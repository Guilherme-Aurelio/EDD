class Fila:

  def __init__(self) -> None:
    self.inicio = None
    self.fim = None
    self.tamanho = 0

  def is_empty(self):
    return self.tamanho == 0

  def put(self, valor):
    novo_no = No(valor)

    if self.is_empty():
      self.inicio = novo_no
    else:
      self.fim.proximo = novo_no

    self.fim = novo_no
    self.tamanho += 1

  def remove(self):
    if self.is_empty():
      raise Exception("A fila está vazia!")

    valor = self.inicio.valor
    self.inicio = self.inicio.proximo
    self.tamanho -= 1

    if self.is_empty():
      self.fim = None

    return valor

  def get(self):
    if self.is_empty():
      raise Exception("A fila está vazia!")

    return self.inicio.valor

  def list_items(self):
    if self.is_empty():
      print("A fila está vazia!")
    else:
      print("Elementos na fila:")

      no_atual = self.inicio
      while no_atual is not None:
        print(no_atual.valor)
        no_atual = no_atual.proximo

  def get_size(self):
    return self.tamanho


class No:

  def __init__(self, valor) -> None:
    self.valor = valor
    self.proximo = None