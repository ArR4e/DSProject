from math import pi
mõõt = 0
while True:
    kook = str(input('Millist kooki soovite? '))
    if kook == str():
        break
    def koogi_hind(kook, mõõt):
        if kook == 'šokolaadikook':
            mõõt = float(input('Mis on koogi raadius sentimeetrites? '))
            šk = pi*float(mõõt)**2
            return round(šk*0.06, 2)
        elif kook == 'ploomikook':
            mõõt = float(input('Mis on koogi raadius sentimeetrites? '))
            pk = pi*float(mõõt)**2
            return round(pk*0.04, 2)
        elif kook == 'Napoleoni kook':
            mõõt = float(input('Mis on koogi küljepikkus sentimeetrites? '))
            N = mõõt**2
            return round(N*0.1, 2)
        else:
            raise Exception('Sellist kooki andmebaasist ei leitud')
    print(koogi_hind(kook, mõõt))
