vana = (input("esialgne fail: "))
uus= (input("uus faili nimi: "))
tekst = open(vana,'r')
loetud_tekst=(tekst.read().lower())
loetud= (loetud_tekst.count("hello"))


uus_fail = (open(uus, "w"))
uus_fail.write(loetud_tekst.replace("hello", "tere"))
uus_fail.close()

kontroll = open(uus, "r")
print(kontroll.read())



       


