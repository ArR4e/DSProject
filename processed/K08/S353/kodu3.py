from film import *
def töötleKäsk(sõne, järjend):
    sõneteisestargumendist=' '.join(järjend)
    if sõne=='K':
        järjendõigetestzanridest=loetleFilmid(sõneteisestargumendist)
        print('võimalikud filmid on:')
        print('\n'.join(järjendõigetestzanridest))
        return True
    elif sõne=='L':
        nimi=' '.join(järjend[1:])
        zanr=järjend[0]
        lisaFilm(nimi, zanr)
        print('Film lisatud.')
        return True
    elif sõne=='V':
        if kustutaFilm(sõneteisestargumendist)==False:
            print('Sellist filmi ei leitud')
        else:
            print('film nimekirjast kustutatud') ; print('Head vaatamist.')
        return True
    elif sõne=='E':
        return False
    else:
        raise Exception('midagi läks nihu')

print("""====== FILMIANDMEBAAS ======
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
============================""")
    
while True:
    try:
        sisend=input('> ').strip()
        if sisend=='E':
            järjend=[]
            sõne=sisend
        else:
            i=sisend.find(' ')
            sõne=sisend[:i].strip()
            järjend=sisend[i+1:].split()
        if töötleKäsk(sõne, järjend):
            continue
        else:
            break
    except:
        print('vigane sisend')