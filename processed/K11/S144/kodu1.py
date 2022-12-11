def seosta_lapsed_ja_vanemad(a, b):
    f1 = open(a) # lapsed.txt
    f2 = open(b) # nimed.txt
    d1 = {}
    d2 = {}
    s = set()
    temp = []
    for i in f2:
        i = i.strip().split(' ', 1)
        d1[i[0]] = i[1]
    for i in f1:
        i = tuple(i.strip().split())
        temp.append(i)
    for i, j in temp:
        # i lapsevanem
        # j laps
        i = d1.get(i)
        lvnimed = d2.get(d1.get(j), set())
        lvnimed.add(i)
        d2[d1.get(j)] = lvnimed
    return d2
andmed = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')
for i in andmed:
    vanemad = list(map(str, andmed[i]))
    vanemad = ', '.join(vanemad)            
    print(f'{i}: {vanemad}')
        