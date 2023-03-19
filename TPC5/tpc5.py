import re

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

def levantar(line):
    global levantado

    if levantado:
        print("O telefone já está levantado")
    else:
        levantado=True
        print("Pode iniciar uma interação")

def pousar(line):
    global dinheiro, levantado
    if not levantado:
        print("Impossível pousar o telefone visto que não foi levantado")
    else:
        troco()
        print("O telefone foi pousado")
        levantado = False
        dinheiro=0

def moedas(line):
    global levantado, dinheiro

    if not levantado:
        print("Impossível inserir moedas")
    else:
        moedas = re.findall(r"\d+[ce]",line)
        money_aux = 0

        for moeda in moedas:
            if moeda[-1] == "e":
                value = int(moeda[:-1]) * 100
            else:
                value = int(moeda[:-1])

            if value not in [1, 2, 5, 10, 20, 50, 100, 200]:
                print(f"maq: \"{moeda} - A moeda introduzida é inválida.\"")

            else:
                money_aux += value

        dinheiro += money_aux

        print(f"maq: \" O seu saldo é : {dinheiro // 100}e{dinheiro - (dinheiro // 100) * 100}c\"")


def numero(line):
    global levantado, dinheiro

    if not levantado:
        print("maq: \"O telefone não foi levantado.\"")
    else:
        numeroTelefone = line[2:][:1]

        if re.fullmatch(r"(00\d{9}|\d{9})", numeroTelefone):
            print("maq: \"Número de telefone inválido.\"")
        elif numeroTelefone.startswith("601") or numeroTelefone.startswith("604"):
            print("maq: \"Esse número não é permitido neste telefone. Queira discar novo número!\"")
        elif numeroTelefone.startswith("00"):
            if dinheiro < 150:
                print("maq: \"Saldo insuficiente.\"")
            else:
                dinheiro -= 150
                print(f"maq: \"saldo = {dinheiro // 100}e{dinheiro - (dinheiro// 100) * 100}c\"")
        elif numeroTelefone.startswith("2"):
            if dinheiro < 25:
                print("maq: \"Saldo insuficiente.\"")
            else:
                dinheiro -= 25
                print(f"maq: \"saldo = {dinheiro // 100}e{dinheiro - (dinheiro // 100) * 100}c\"")
        elif numeroTelefone.startswith("808"):
            if dinheiro < 10:
                print("maq: \"Saldo insuficiente.\"")
            else:
                dinheiro -= 10
                print(f"maq: \"saldo = {dinheiro // 100}e{dinheiro - (dinheiro // 100) * 100}c\"")
        else:
            print(f"maq: \"saldo = {dinheiro // 100}e{dinheiro - (dinheiro // 100) * 100}c\"")


def abortar(line):
    global levantado, dinheiro

    if not levantado:
        print("Impossível abortar")
    else:
        troco()
        dinheiro=0

def main():
    comandos = {"LEVANTAR": levantar,
                "POUSAR": pousar,
                "MOEDA": moedas,
                "T": numero,
                "ABORTAR": abortar}

    while True:
        line = input()
        for key,value in comandos.items():
            if line.startswith(key):
                value(line)

if __name__ == '__main__':
    main()


