#programm saab kasutajalt failide nimed
lähtefail = input("Lähtefaili nimi: ")
sihtfail = input("Sihtfaili nimi: ")
#programm avab failid (loob uue sihtfaili, kui seda pole/teeb eelnevalt eksisteerinu tühjaks)
LÄHTEFAIL = open(lähtefail, "r")
SIHTFAIL = open(sihtfail, "w")
#programm teeb failist sõne
tekst = LÄHTEFAIL.read()
#loetakse kokku, mitu asendust on vaja teha ja asendused sooritatakse
asendusi = tekst.count("Hello")
uus_tekst = tekst.replace("Hello","Tere")
#tekst kirjutatakse sihtfaili
SIHTFAIL.write(uus_tekst)
#failid suletakse
SIHTFAIL.close()
LÄHTEFAIL.close()
#asenduste arv väljastatakse
print("Tehti", asendusi, "asendamist.")