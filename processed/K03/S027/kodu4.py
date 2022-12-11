f = open('kinganumbrid.txt')
viga = str('vigane sisend')
s = f.readline()
while s != str():
    try:
        s = float(s)
        pikkus = round(2/3*(s-2))
        print(pikkus)
        s = f.readline()
    except:
        print(viga)
        s = f.readline()