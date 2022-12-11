f1 = input("Lähtefaili nimi: ")
f2 = input("Sihtfaili nimi: ")

f = open(f1)
data = f.read()
asendus = data.count("Hello")
data = data.replace("Hello", "Tere")
f.close()

f = open(f2, "w")
f.write(data)
f.close()

print("Tehti", str(asendus), "asendamist.")