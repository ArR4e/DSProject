info2 = {}

def seosta_lapsed_ja_vanemad(a, b):
    info1 = {}
    l1 = []
    l2 = []
    with open(b) as f2:
        for line in f2:
            line = line.strip()
            l2.append((line.split(' ', 1)))
    with open(a) as f1:
        for line in f1:
            line = line.strip()
            l1.append(line.split(' ', 2))
    for element in l2:
        info1[element[0]] = element[1]
    for element in l1:
        if element[1] in info1:
            info2.setdefault(info1[element[1]],set()).add(info1[element[0]])
    return info2

seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')
    
for key, value in info2.items():
    print(key + ':', ', '.join(value))