'''
Kirjuta funktsioon koogi_hind, mis võtab argumentideks koogi nime ning mõõdu
ja tagastab koogi maksumuse eurodes, ümardatult teise komakohani
'''
from math import pi

def koogi_hind (kook, mõõt):
    
    if kook!= 'šokolaadikook' and kook!= 'ploomikook' and kook!= 'Napoleoni kook':
        raise Exception('Sellist kooki andmebaasist ei leitud')
    #juhul kui sisestatakse vale kook, siis annab veateate käsureale
    
    if kook== 'šokolaadikook' or kook== 'ploomikook': #ümarate kookide puhul võtab selle valemi
        pindala= pi*mõõt**2
        if kook== 'šokolaadikook':
            hind= 0.06
            return round(pindala* hind, 2)
        if kook== 'ploomikook':
            hind= 0.04
            return round(pindala* hind, 2)
    else:
        kook== 'Napoleoni kook' #kui pole ümar kook, võtab selle valemi
        pindala= mõõt**2
        hind= 0.1
        return round(pindala* hind, 2)

while True:
    
    nimi= input('Sisesta koogi nimi:')
    if nimi == '':
        break
    # lihtsalt Enteri vajutusega väljub programmist
    mõõt= float(input('Sisesta koogi mõõt:'))
    
    print('Sisestatud mõõduga '+ nimi.replace('kook', 'koogi ')\
          +'hind on '+ str(koogi_hind(nimi, mõõt))+'€')
    #vahelduse mõttes tegin plussidega, siis peab meeles pidama, et tühikud lisada
    # ja arvud sõnedeks muuta
    print('ˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ')
    