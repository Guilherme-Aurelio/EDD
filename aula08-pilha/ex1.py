from pilha import Pilha

def ConversaoDecimal(dec,base):
    digitos = "0123456789ABCDEF"

    pilha = Pilha()

    while dec > 0:
        num = dec % base
        pilha.push(num)
        dec = dec // base

    str = ""
    while not pilha.is_empty():
        str = str + digitos[pilha.pop()]

    return str

pilha = Pilha()

resultado_octal = ConversaoDecimal(256, 8)
pilha.push(resultado_octal)
print("Resultado em octal:", resultado_octal)

resultado_hexadecimal = ConversaoDecimal(256, 16)
pilha.push(resultado_hexadecimal)
print("Resultado em hexadecimal:", resultado_hexadecimal)

def conversao_para_decimal(num, base):
    digitos = "0123456789ABCDEF"
    potencia = 0
    dec = 0
    
    num_str = str(num)
    
    for i in range(len(num_str)-1, -1, -1):
        digito = digitos.index(num_str[i])
        
        dec += digito * base**potencia
        
        potencia += 1
    
    return dec

dec = conversao_para_decimal("1A", 16)
print(dec)

dec = conversao_para_decimal("32", 8)
print(dec)
