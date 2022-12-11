def seosta_lapsed_ja_vanemad(laste_fail, nimede_fail):
    ids = {}
    relations = {}
    f = open(nimede_fail, encoding='utf-8')
    lines = f.readlines()
    f.close()
    for i in lines:
        ids[i.split()[0]] = " ".join(i.split()[1:])
    f = open(laste_fail)
    lines = f.readlines()
    f.close()
    for i in lines:
        pair = i.rstrip().split()
        if ids[pair[1]] in relations:
            relations[ids[pair[1]]].add(ids[pair[0]])
        else:
            relations[ids[pair[1]]] = {ids[pair[0]]}
    return relations

relations = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')

for i, j in relations.items():
    print(i + ':', ', '.join(j))