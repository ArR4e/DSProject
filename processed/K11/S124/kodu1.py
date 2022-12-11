def seosta_lapsed_ja_vanemad(f1, f2):
#https://www.geeksforgeeks.org/python-convert-a-list-to-dictionary/
    def convert(a):
        it = iter(a)
        res_dct = dict(zip(it, it))
        return res_dct
    
    f1 = open("lapsed.txt", encoding = 'utf-8')
    f2 = open("nimed.txt", encoding = 'utf-8')

    j = []
    ik = {}
    
    for rida in f2:
        rida = rida.strip().split(" ", 1)
        for el in rida:
            j += [el]
    s = convert(j)
    
    for rida in f1:
        rida = rida.strip().split()
        ik_vanem = rida[0]
        vanem = s.get(ik_vanem)
        ik_laps = rida[1]
        laps = s.get(ik_laps)
        isikud = ik.get(laps, set())
        isikud.add(vanem)
        ik[laps] = isikud

    f1.close()
    f2.close()
    
    return ik
    
#print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))