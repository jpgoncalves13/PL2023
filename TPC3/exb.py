import re

def calculate_cent(year):
    sec = year[0:2]
    if year[2] == 0 and year[3] == 0:
        return sec
    else:
        return str(int(sec)+1)

def main():
    file = open("processos.txt","r")
    lines = file.readlines()
    years_er = re.compile(r"\d+::(\d{4})-")
    names_er = re.compile(r"::([A-Z][a-z]+) [A-Za-z]* ([A-Z][a-z]+)::")

    cents = {}

    for line in lines:
        year = years_er.match(line)
        names = names_er.findall(line)

    if year:
        for name in names:
            cent = calculate_cent(year.group(1))
            if cent not in cents:
                cents[cent] = {}
                (cents[cent])["nomesP"] = {}
                (cents[cent])["Apel"] = {}

            nomeP, Apel = name

            if nomeP in (cents[cent])["nomesP"]:
                cents[cent]["nomesP"][nomeP] += 1
            else:
                cents[cent]["nomesP"][nomeP] = 1

            if Apel in (cents[cent])["Apel"]:
                cents[cent]["Apel"][Apel] += 1
            else:
                cents[cent]["Apel"][Apel] = 1

    for century in cents:
        print('-' * 5 + 'Século ' + century + '-' * 5 + '\n')
        print('Top 5 nomes:')

        sorted_first_names = sorted(((cents[century])['nomes']).items(), key=lambda x: x[1], reverse=True)
        for i in range(5):
            print(sorted_first_names[i])

        print('\nTop 5 apelidos:')
        sorted_last_names = sorted(((cents[century])['apelidos']).items(), key=lambda x: x[1], reverse=True)
        for i in range(5):
            print(sorted_last_names[i])

        print()



if __name__ == '__main__':
    main()