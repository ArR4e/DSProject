ing = input("Lähtefaili nimi: ")
est = input("Sihtfaili nimi: ")
f = open(ing)
n = f.read()
mitu = n.count("Hello")
f.close()

m = n.replace("Hello", "Tere")

a = open(est, "w")
k = a.write(m)
a.close()

print("Tehti", mitu, "asendust")