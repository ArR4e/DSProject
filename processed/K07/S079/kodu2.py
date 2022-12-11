# 2. Taksohinnad
# Tiiu juures sai pidu läbi ja inimesed hakkavad koju liikuma.
# Failis taksohinnad.txt on kirjas taksode nimi, sisseistumise hind ja kilomeetri hind, eraldatult komadega.

# Kirjuta programm, mis küsib kasutajalt tee pikkuse koju kilomeetrites ning väljastab vastavalt failis olevatele
# hindadele kõige odavama takso nime.

# Näide
# Faili taksohinnad.txt sisu:

# Maksitaksi,2.0,0.6
# Sõps veab,10,0
# Waldo takso,1.0,1.0
#  Sisesta tee pikkus kilomeetrites: 7
#  Kõige odavam on Maksitaksi.
# Automaatkontroll. Programm peab kasutajalt küsima täpselt ühte sisestust: tee pikkust kilomeetrites.
# Failinimi taksohinnad.txt tuleks kirjutada programmi sisse; automaatkontroll eeldab, et andmeid loetakse selle nimega failist.
# Töö lõpus väljastada ekraanile kõige odavama taksofirma nimi.

km_input = float(input("Sisesta tee pikkus kilomeetrites: "))

try:
    f = open("taksohinnad.txt", "r")
    taksod = []
    hinnad = []
    while True:
        rida = f.readline()
        if rida == "":
            break
        else:
            rida1 = rida.strip().split(",")
            takso = rida1[0]
            sisse = float(rida1[1])
            km_hind = float(rida1[2])
            hind_kokku = sisse + (km_hind * km_input)
            taksod.append(takso)
            hinnad.append(hind_kokku)
    print(taksod[hinnad.index(min(hinnad))])
except:
    print("Taksod puuduvad")
f.close()

