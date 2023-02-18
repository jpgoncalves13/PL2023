def validar_sexo(sexo):
    return sexo == "M" or sexo == "F"

def validar_inteiro(numero):
    for c in numero:
        if not c.isdigit():
            return False
    
    return True

def validar_bit(bit):
    return bit == "0" or bit == "1"
