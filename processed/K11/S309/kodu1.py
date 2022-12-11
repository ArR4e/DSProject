def seosta_lapsed_ja_vanemad(kidsfilename, namesfilename):

    d = dict()
    namesDict = dict()

    with open(namesfilename, 'r', encoding="UTF-8") as namesfile:
        
        for line in namesfile:
            linelist = line.strip().split()
            
            name = ''
            for i,j in enumerate(linelist):
                if i == 0:
                    continue
                else:
                    name = name + " " + str(j)

            namesDict[linelist[0]] = name

    with open(kidsfilename, 'r', encoding="UTF-8") as kidsfile:
        
        for line in kidsfile:
            linelist = line.strip().split()
            
            if namesDict[linelist[1]] in d:
                d[namesDict[linelist[1]]].add(namesDict[linelist[0]])
            else:
                d[namesDict[linelist[1]]] = set()
                d[namesDict[linelist[1]]].add(namesDict[linelist[0]])

    return d

print(seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt'))