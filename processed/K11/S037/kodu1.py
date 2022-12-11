def seosta_lapsed_ja_vanemad(fail1, fail2):
    f1 = open(fail1, 'r')
    f2 = open(fail2,'r')
    nimed = {}
    lapsed = {}
    for rida in f2:
        n = rida.strip().split()
        e = n[0]
        n.remove(e)
        nimed[e] = ' '.join(map(str,n))
    for rida in f1:
        m = rida.strip().split()
        if nimed[m[1]] not in lapsed:
            lapsed[nimed[m[1]]] = set()
            lapsed[nimed[m[1]]].add(nimed[m[0]])
        else:
            lapsed[nimed[m[1]]].add(nimed[m[0]])
    f1.close()
    f2.close()
    return lapsed

sõnastik = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')
for võti in sõnastik:
    l = ''
    k = []
    for el in sõnastik[võti]:
        if len(sõnastik[võti]) == 1:
           l += el
        else:
            k += [el]
    if l == '':
        a = ', '.join(k)
        print(f'{võti}: {a}')
    else:
        print(f'{võti}: {l}')