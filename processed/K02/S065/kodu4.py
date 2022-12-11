a = input("Lähtefaili nimi: ")
b = input("Sihtfaili nimi: ")

faila = open(a, encoding="UTF-8")
failb = open(b, "w", encoding="UTF-8")

i=0 #enne for tsüklit tuleb luua muutuja, mis võrdub 0-ga
#hakkab lisama sellele 0-le, mitu korda tehti asendusi

for rida in faila: #eraldab inglise.txt failist read
    failb.write(rida.replace("Hello", "Tere")) #asendab fail(a,b) tekstid
    i += rida.count("Hello") #rida.count vaatab üle kõik read ja loeb kokku need kohad, kus asendused toimusid
    
faila.close()
failb.close()

print("Tehti",i,"asendust.")