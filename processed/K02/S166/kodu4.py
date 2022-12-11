lähte = input("Sisesta tõlgitava faili täpne nimi: ")
tõlge = input("Sisesta uue faili nimi: ")

f = open(lähte, "r")


s = open(tõlge, "wt")
for line in f:
    s.write(line.replace("Hello", "Tere"))
f = open(lähte, "r")
a = f.read()
b = a.count("Hello")

print("Tehti ", b, " asendamist.")

f.close()
s.close()