from pilha import Pilha

def ConversaoDecimal(decNumber,base):
    digitos = "0123456789ABCDEF"

    pilha = Pilha()

    while decNumber > 0:
        num = decNumber % base
        pilha.push(num)
        decNumber = decNumber // base

    newString = ""
    while not pilha.is_empty():
        newString = newString + digitos[pilha.pop()]

    return newString

print(ConversaoDecimal(256,16))
print(ConversaoDecimal(25,16))

