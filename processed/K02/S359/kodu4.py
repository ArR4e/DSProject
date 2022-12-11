a=input("Lähtefaili nimi: ")
b=input("Sihtfaili nimi: ")

f=open(a, "r")
faili_sisu = f.read()
hello_arv=faili_sisu.count("Hello")
vahetus = faili_sisu.replace("Hello", "Tere")
f.close()

g=open(b, "w+")
faili_sisu2 = g.read()
g.write(vahetus)
g.close()


print("Tehti",hello_arv,"asendamist!")