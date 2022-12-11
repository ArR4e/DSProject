import math
def koogi_hind(nimi, mõõt):
    while nimi != '':
        mõõt = float(mõõt)
        for i in range(1):
            if nimi == 'šokolaadikook':
                suurus = math.pi * mõõt ** 2
                print(round(suurus * 0.06, 2))
                nimi = input('Sisesta koogi nimi:')
                if nimi == '':
                    break
                else:
                   mõõt = input('Sisesta koogi mõõt:') 
                break            
            if nimi == 'ploomikook':
                suurus = math.pi * mõõt ** 2
                print(round(suurus * 0.04, 2))
                nimi = input('Sisesta koogi nimi:')
                if nimi == '':
                    break
                else:
                   mõõt = input('Sisesta koogi mõõt:')
                break
            if nimi == 'Napoleoni kook':
                suurus = mõõt * mõõt
                print(round(suurus * 0.1, 2))
                nimi = input('Sisesta koogi nimi:')
                if nimi == '':
                    break
                else:
                   mõõt = input('Sisesta koogi mõõt:')
                break
            else:
                print('Sellist kooki andmebaasist ei leitud.')
                nimi = input('Sisesta koogi nimi:')
                if nimi == '':
                    break
                else:
                   mõõt = input('Sisesta koogi mõõt:')
nimi = input('Sisesta koogi nimi:')
mõõt = input('Sisesta koogi mõõt:')
koogi_hind(nimi, mõõt)