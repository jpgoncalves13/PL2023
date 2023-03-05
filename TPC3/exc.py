import re

def main():
    file = open("processos.txt","r")
    lines = file.readlines()

    relationships = re.compile(r"[a-z],([A-Z][a-zA-Z ]*?)\.")
    relationshipsDict = {}

    for line in lines:
        relationships_list = relationships.findall(line)

        for relationship in relationships_list:
            if relationship not in relationshipsDict:
                relationshipsDict[relationship] = 0
            relationshipsDict[relationship] += 1

    print(relationshipsDict)


if __name__ == '__main__':
    main()
