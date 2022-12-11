#defineerin funktsiooni, mis otsib kooki ja leiab selle hinna
def koogi_hind(nimi, mõõt):
    try: 
        if nimi == 'šokolaadikook':
            x = round((mõõt**2*3.141592653*0.06), 2)
        elif nimi == 'ploomikook':
            x =  round((mõõt**2*3.141592653*0.04), 2)
        elif nimi == 'Napoleoni kook':
            x = round((mõõt**2*0.1), 2)
    except:
        x = 'Sellist kooki andmebaasist ei leitud'
    finally:
        return x
#põhiprogramm
while True:
    kook = input('Milline kook? ')
    #juhul kui vajutatakse lihtsalt ENTER'it siis programm lõpeb
    if kook == '':
        break
    mõõt = float(input('Mõõt? '))
    print(koogi_hind(kook, mõõt))

    