


lähtefail = input("sisesta lähtefail: ")
lõppfail = input("sisesta lõppfail: ")

esimene_fail = open(lähtefail, "rt")
inglise_tekst = esimene_fail.read()
#print(type(inglise_tekst))
esimene_fail.close()

asendus = inglise_tekst.count("Hello")
print("\n")
print("lähtefail: " + lähtefail)
print("sihtfail: " + lõppfail)
print(f"Toimus {asendus} asendust")
eesti_tekst = inglise_tekst.replace("Hello", "Tere")


teine_fail = open(lõppfail, "wt")
eesti_tekst = teine_fail.write(eesti_tekst)
#print(eesti_tekst) miks ta annab vastuseks 32 ????



teine_fail.close()


