import re

def main():
    file = open("processos.txt","r")
    lines = file.readlines()
    er = re.compile(r"\d+::(\d{4})-")
    years = {}

    for line in lines:
        if er.match(line):
            year = er.match(line).group(1)
            if year in years:
                years[year] += 1
            else:
                years[year] = 1

    for chave in years:
        print(chave + ":" + str(years[chave]))

if __name__ == '__main__':
    main()
