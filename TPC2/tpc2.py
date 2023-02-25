linha = input(">")
soma = 0

aux=""
state = True #ligado
auxState = ""

for c in linha:
    c = c.upper()

    if state == True:
        if '0' <= c <= '9':
            aux+=c
        else:
            if len(aux) != 0:
                soma += int(aux)
                aux=""

    if c == "O":
        auxState = c
        
    elif c == "N" and auxState == "O":
        state = True 
        auxState = ""

    elif c == "F" and auxState == "OF":
        state = False
        auxState = ""

    elif c == "F" and auxState == "O":
        auxState += c

    elif c == "=":
        print(soma)


