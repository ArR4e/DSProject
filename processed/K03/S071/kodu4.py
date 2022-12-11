#Kirjuta programm, mis loeb tekstifailist kinganumbrid.txt sisse EU kinganumbrid ja kuvab ekraanile vastavad jalalaba pikkused sentimeetrites ümardatuna täisarvuks.
#Valem jalalaba pikkuse arvutamiseks on: pikkus = 2/3 * (kinganumber - 2).
#Faili nende ridade juures, kus arvuks teisendamine miskipärast ebaõnnestub, tuleb ekraanile kuvada „Vigane sisend” ning jätkata faili järgmise reaga.

#Programm ei küsi kasutajalt midagi, andmed loetakse alati sisse failist kinganumbrid.txt.
#Tekstifailis tähistab iga rida ühte kinganumbrit.
#Arvud võivad olla ühe komakohaga murdarvud, sel juhul on kümnenderaldajana kasutatud punkti (kuna seda on Pythonis lihtsam ujukomaarvuks teisendada).
#Mõnedel ridadel võib olla mingi jama. Väljundis peab iga kinganumber (või tekst „Vigane sisend”) olema eraldi real.

f = open("kinganumbrid.txt", "r")
for rida in f:
    try:
        print(round(2 / 3 * (float(rida) - 2)))
    except:
        print("Vigane sisend")

f.close()
