#Masintõlge

#Kirjuta programm, mis küsib kasutajalt kaks failinime.
#Esimene märgib mingit olemasolevat tekstifaili, teine aga mingit uut faili, mida ei tarvitse veel olemas olla.
#Programmi ülesanne on 1) võtta esimese faili sisu, 2)asendada seal kõik sõnad „Hello" sõnadega „Tere“ ja 3)kirjutada tulemus teise faili.
#Ekraanile väljastada, mitu asendamist tehti.

#vihje: kasuta "count" liitfunktsiooni, mis aitab str tähti lugeda.
esialgne_tekstifail = input(print("Kirjuta siia esialgse faili nimi."))
uus_tekstifail = input(print("Kirjuta siia uue faili nimi."))


Hello_txt = open(str(esialgne_tekstifail), 'r')
#koma eristab sekundaarset käsku/funktsiooni funktsioonis
faili_sisu = Hello_txt.read()
#tühjad sulud on olulised, kuna nende sisse saab minna faili sisu
#kui oleks readline, siis saaks failist juba rea võtta, mitte tervet faili
print(faili_sisu)

#asendamis liitfunktsioon on "replace". see on kujul string.replace(old, new, count)

faili_sisu2 = faili_sisu.replace("Hello", "Tere")

print(faili_sisu2)

uus_fail = open(str(uus_tekstifail), "w")
uus_fail.write(faili_sisu2)
uus_fail.close()
Hello_txt.close()
#jällegi toonitan: sulud annavad sisu sisse. See on nagu end of function ehk ka.

#mitu asendust tehti
Hello_txt = open(str(esialgne_tekstifail), 'r')
faili_sisu3 = Hello_txt.read()
Tere_txt = open(str(uus_tekstifail), "r")
faili_sisu4 = Tere_txt.read()

print(int(faili_sisu4.count("Tere"))-int(faili_sisu.count("Tere")))



#Huvitav1
# Lugemine veebist
#Ka veebist teksti lugemine pole eriti raske – käsu open asemel tuleb kasutada käsku urlopen, mis on vaja eelnevalt importida moodulist urllib.request:

#from urllib.request import urlopen

#vastus = urlopen("http://artscene.textfiles.com/asciiart/simpsons.txt")

#baidid = vastus.read()
# veebist lugemisel annab käsk read() meile tavalise sõne asemel hunniku baite,
# mis on vaja veel sõneks "dekodeerida"
#tekst = baidid.decode()

#print(tekst)

#vastus.close()


#Huvitav2
#Juhuslike täisarvude genereerimiseks tuleb importida käsk randint moodulist random. Järgnev lühike programm kuvab ekraanile ühe juhusliku arvu vahemikust 1..100:

#from random import randint
#print(randint(1, 100))