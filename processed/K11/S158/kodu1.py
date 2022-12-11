l = open("lapsed.txt", encoding="UTF-8")
n = open("nimed.txt", encoding="UTF-8")

def seosta_lapsed_ja_vanemad(l, n) :
    a = {}
    b = {}
    q = {}
    for rida in n:
        r = rida.strip().split()
        nimi = r[1] + " " + r[2]
        a[r[0]] = nimi
    #print(a)

    for rida in l:
        s = rida.strip().split()
        vanem = s[0]
        laps = s[1]
        vanemad = b.get(laps, set())
        vanemad.add(vanem)
        b[laps] = vanemad
    #print(b)
        
    for key in b.keys():
        võti = a.get(key)
        d = set()
        for el in b.get(key):
            d.add(a.get(el))
        q[võti] = d
    return q
               
print(seosta_lapsed_ja_vanemad(l, n))                
l.close()
n.close()