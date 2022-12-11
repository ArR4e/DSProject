# Tiiu juures sai pidu läbi ja inimesed hakkavad koju liikuma. Failis taksohinnad.txt on kirjas taksode nimi,
# sisseistumise hind ja kilomeetri hind, eraldatult komadega. Kirjuta programm, mis küsib kasutajalt tee pikkuse koju
# kilomeetrites ning väljastab vastavalt failis olevatele hindadele kõige odavama takso nime.
# 
# Näide
# Faili taksohinnad.txt sisu:
# 
# Maksitaksi,2.0,0.6
# Sõps veab,10,0
# Waldo takso,1.0,1.0
# Sisesta tee pikkus kilomeetrites: 7
# Kõige odavam on Maksitaksi.
# Automaatkontroll. Programm peab kasutajalt küsima täpselt ühte sisestust: tee pikkust kilomeetrites.
# Failinimi taksohinnad.txt tuleks kirjutada programmi sisse; automaatkontroll eeldab, et andmeid loetakse
# selle nimega failist. Töö lõpus väljastada ekraanile kõige odavama taksofirma nimi.

pikkus = int(input("Sisesta tee pikkus kilomeetrites "))
fail = open('taksohinnad.txt','r')
lõpphind = [0]
hind = stardihind + kilomeetrite_arv*kilomeetri_tasu

lug_info = str(file)
info = lug_info.split(",")

taksode_hinnad.append(takso_hind)
nimed.append(nimi)
indeks = 0
    miinimum = järjend[0]
    for i in range(len(järjend)):
        if järjend[i] < miinimum:
            miinimum = järjend[i]
            indeks = i


try:
    kilomeetrid = float(lug_info[2])
    