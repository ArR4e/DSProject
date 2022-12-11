from math import pi

def koogi_hind(nimi,moot):
    if nimi==('šokolaadikook'):
        return 0.06*moot**2*pi
    elif nimi==('ploomikook'):
        return 0.04*moot**2*pi
    elif nimi==('Napoleoni kook'):
        return 0.1*moot**2
    else:
        raise Exception ('Sellist kooki andmebaasist ei leitud')

try:
    while True:
        nimi=input('Sisesta koogi nimi:')
        moot=float(input('Sisesta koogi mõõt:'))
        print(round(koogi_hind(nimi,moot),2))
        
except:
    print('Külastage meid jälle!')
    
    
