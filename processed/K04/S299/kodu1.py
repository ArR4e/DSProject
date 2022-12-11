from math import pi


def koogi_hind(nimi, mõõt):
    if nimi == 'šokolaadikook':
        return round((0.06*(mõõt**2*pi)),2)
    else:
        if nimi== 'ploomikook':
            return round((0.04*(mõõt**2*pi)),2)
        else:
            if nimi== 'Napoleoni kook':
                return round(0.1*mõõt**2)
            else:
                print('Sellist kooki andmebaasist ei leitud')
            
nimi= str(input('Sisestage koogi nimi: '))


mõõt= int(input('Sisestage koogi mõõt sentimeetrites: '))


print(koogi_hind(nimi, mõõt))
          
#sain vist ülesandest veidi teisiti aru        
    
    