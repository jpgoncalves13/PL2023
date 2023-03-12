import re
import statistics
import json
import sys

json_list = []
validators_list = []
fields_list = []

csv_file = open(sys.argv[1],"r")

lines = list(csv_file.readlines())

matches = re.finditer(r"(\w+)(?:\{(\d+)(?:,(\d+))?})?(?:::)?(\w+)?", lines[0]) # Fazer regex da primeira linha

for match in matches:
    # Group 1: Name
    # Group 2: Size / min_size
    # Group 3: max_size
    # Group 4: modifiers
    fields_list.append(match.group(1))
    if (match.group(2) != None):
        data_string = r""
        for i in range(0,int(match.group(2))):
            data_string += r",(\d+)"
        if (match.group(3) != None):
            for i in range(int(match.group(2)),int(match.group(3))):
                data_string += r",(\d+)?"
        if (match.group(4) != None):
            validators_list.append((data_string,match.group(4)))
        else:
            validators_list.append((data_string,None))

    else:
        data_string = r"([\w ]+)"
        validators_list.append((data_string,None))

for line in lines[1:]:
    tam = len(fields_list)

    obj = {}
    for i,(validator,calc) in enumerate(validators_list):
        if validator == r"([\w ]+)":
            splits = re.split(r"([\w ]+)", line, 1)
            line = splits[2]
            obj[fields_list[i]] = splits[1]
        else:
            splits = re.split(validator, line, 1)
            line = splits [-1]
            list = []
            for s in splits[1:len(splits)-1]:
                if s is not None:
                    list.append(int(s))

            save = fields_list[i] #guardar o valor do campo
            value = None

            if calc == 'media':
                value = statistics.mean(list)
                fields_list[i] = fields_list[i] + "_media"
            elif calc == 'sum':
                value = sum(list)
                fields_list[i] = fields_list[i] + "_sum"
            elif calc == 'min':
                value = min(list)
                fields_list[i] = fields_list[i] + "_min"
            elif calc == 'max':
                value = max(list)
                fields_list[i] = fields_list[i] + "_max"
            elif calc == 'moda':
                value = statistics.mode(list)
                fields_list[i] = fields_list[i] + "_moda"
            elif calc == None:
                value = list

            obj[fields_list[i]] = value

            fields_list[i] = save

    if line == "\n" or line == "":  # Se não existe mais nada para ler
        json_list.append(obj)

with open(sys.argv[1][:-4] + ".json",'w') as json_file:
    json.dump(json_list, json_file, indent=4, ensure_ascii=False)
