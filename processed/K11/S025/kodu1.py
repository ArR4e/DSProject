def seosta_lapsed_ja_vanemad(a, b):
    f1 = open(a, encoding='utf-8')
    f2 = open(b, encoding='utf-8')
    d = {}
    d1 = {}
    for rida in f2:
        l = rida.strip().split()
        d1[l[0]] = ' '.join(l[1:])
    for rida in f1:
        k = rida.strip().split()
        laps = d1[k[1]]
        vanem = d1[k[0]]
        vanemad = d.get(laps, set())
        vanemad.add(vanem)
        d[laps] = vanemad
    f1.close()
    f2.close()
    return d
idk = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')
for nimi in idk:
    print(nimi+': '+", ".join(idk[nimi]))