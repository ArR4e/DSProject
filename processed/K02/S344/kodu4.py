f = open(input("Sisesta esimese faili nimi: "))
x = input("Sisesta teise faili nimi: ")

a = f.read()

muutuste_arv = a.count("Hello")
print("Failis tehti ", muutuste_arv, "mutatust")

y = open(x, "w+")
y.write(a.replace("Hello","Tere"))
y.close()