#Sisestatav lähtefaili nimi peab olema täpselt sama, mis kaustas oleva faili nimi 
inglise = str(input("Sisesta lähtefaili nimi: "))
eesti = str(input("Sisesta sihtfaili nimi: "))

#Programm avab olemasoleva lähtefaili inglise.txt, loeb kogu sisu ja "Hello" koguse

f = open(inglise)
inglise_sisu = f.read()
asendused=inglise_sisu.count("Hello")

#Proramm tekitab sihtfaili nimega mille kasutaja sisestas, kirjutab kogu lähtefaili sisu ja asendab "Hello" terega 

d=open(eesti, "w")
d.write(inglise_sisu.replace ("Hello", "Tere"))

d.close()
f.close()

#Väljastab asenduste arvu (ehk Hello koguse lähtefailis)

print("Tehti " + str(asendused) + " asendust")







