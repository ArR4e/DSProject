avatav_fail=input("Sisesta faili nimi, mida soovid muuta: "+"\n")
f=open(str(avatav_fail))
faili_sisu=f.read()
f.close()

print("\n"+"Esialgse faili sisu:\n"+faili_sisu)

uus_fail=input("\n"+"Sisesta faili nimi, kuhu soovid muudetud andmed salvestada: "+"\n")

uue_faili_sisu=faili_sisu.replace("Hello","Tere")

f=open(str(uus_fail), "w")
f.write(uue_faili_sisu)
f.close()



print("\n"+"Uue faili sisu:\n"+uue_faili_sisu)

asenduste_arv=faili_sisu.count("Hello")
print("\n"+"Kokku asendati "+ str(asenduste_arv) + " sõna.")






         

