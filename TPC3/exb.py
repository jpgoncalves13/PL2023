import re


def calculate_cent(year):
    sec = year[0:2]
    if year[2] == 0 and year[3] == 0:
        return sec
    else:
        return str(int(sec) + 1)


def main():
    with open("processos.txt", "r") as file:
        lines = file.readlines()

    er_years = re.compile(r"\d+::(\d{4})-")
    er_names = re.compile(r"::([A-Z][a-z]+) [a-zA-Z ]*([A-Z][a-z]+)::")

    centuries = {}

    for line in lines:
        year = er_years.match(line)
        names_list = er_names.findall(line)

        if year:
            for name in names_list:
                century = calculate_cent(year.group(1))
                if century not in centuries:
                    centuries[century] = {}
                    (centuries[century])['nomesProp'] = {}
                    (centuries[century])['apelidos'] = {}

                first_name, last_name = name

                if first_name in ((centuries[century])['nomesProp']):
                    ((centuries[century])['nomesProp'])[first_name] += 1
                else:
                    ((centuries[century])['nomesProp'])[first_name] = 1

                if last_name in ((centuries[century])['apelidos']):
                    ((centuries[century])['apelidos'])[last_name] += 1
                else:
                    ((centuries[century])['apelidos'])[last_name] = 1

    for century in centuries:
        print('-' * 5 + 'Século ' + century + '-' * 5 + '\n')
        print('Top 5 nomes:')

        sorted_first_names = sorted(((centuries[century])['nomesProp']).items(), key=lambda x: x[1], reverse=True)
        for i in range(5):
            print(sorted_first_names[i])

        print('\nTop 5 apelidos:')
        sorted_last_names = sorted(((centuries[century])['apelidos']).items(), key=lambda x: x[1], reverse=True)
        for i in range(5):
            print(sorted_last_names[i])

        print()


if __name__ == '__main__':
    main()