
levantado = False
dinheiro=0

def troco():
    global dinheiro

    moedas = {1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0, 200: 0}

    for moeda in [200, 100, 50, 20, 10, 5, 2, 1]:
        if dinheiro <= 0:
            break
        valor = dinheiro // moeda
        moedas[moeda] += valor
        dinheiro -= valor * moeda

    print(f"maq: \"O seu troco é = {moedas[200]}x2e, {moedas[100]}x1e, {moedas[50]}x50c, {moedas[20]}x20c, {moedas[10]}x10c, {moedas[5]}x5c, {moedas[2]}x2c, {moedas[1]}x1c;\"")

def levantar():
    global levantado

    if levantado:
        print("O telefone já está levantado")
    else:
        levantado=True
        print("Pode iniciar uma interação")

def pousar():
    global dinheiro, levantado
    if not levantado:
        print("Impossível pousar o telefone visto que não foi levantado")
    else:
        troco()
        print("O telefone foi pousado")
        levantado = False
        dinheiro=0

def moedas():

def numero():

def abortar():
    global levantado, dinheiro

    if not levantado:
        print("Impossível abortar")
    else:
        troco()
        dinheiro=0

def main():
    comandos = {"LEVANTAR": levantar,
                "POUSAR": pousar,
                #"MOEDAS": moedas,
                #"T": numero,
                "ABORTAR": abortar}

    while True:
        line = input()
        for key,value in comandos.items():
            if line.startswith(key):
                value()

if __name__ == '__main__':
    main()


