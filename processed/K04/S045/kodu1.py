from math import pi
def koogi_hind(nimi, mõõt):
    koogid = [('šokolaadikook', 0.06), ('ploomikook', 0.04), ('napoleoni kook', 0.1)]
    
    i = 0
    leitud = False
    for kook in koogid:
        if kook[0].lower() == nimi.lower():
            leitud = True
            if i <= 1:
                suurus = pi * mõõt**2
            else:
                suurus = mõõt**2
            hind = round(suurus * kook[1], 2) #ümardame
            print('Kook maksab', hind, 'eurot')
            return hind
        i += 1
    if leitud == False:
        raise Exception("Sellist kooki andmebaasist ei leitud")

while True:
    nimi = input('Sisesta koogi nimi: ')
    if nimi == "":
        break
    mõõt = float(input('Sisesta koogi mõõt: '))
    koogi_hind(nimi, mõõt)
    