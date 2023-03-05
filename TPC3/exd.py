import re
import json


def main():
    file = open("processos.txt","r")
    lines = file.readlines()

    er = re.compile(r"(?P<pasta>\d+)::(?P<data>\d{4}-\d{2}-\d{2})::(?P<nome>[A-Za-z ]+)::(?P<pai>[A-Za-z ]+)::(?P<mae>[A-Za-z ]+)::(?P<observacoes>.*)::$")

    processos = []
    for i in range(20):
        match = er.match(lines[i])
        if match:
            process = {'pasta': match.group('pasta'), 'data':match.group('data'), 'nome': match.group('nome'),
                       'pai': match.group('pai'), 'mãe': match.group('mae'),
                       'observacoes': match.group('observacoes')}
            processos.append(process)

    fileOut = open("processos.json","w")
    json.dump(processos, fileOut, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()