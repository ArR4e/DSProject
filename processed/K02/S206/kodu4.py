f1 = input("Lähtefaili nimi: ")
f2 = input("Sihtfaili nimi: ")

with open(f1, "r") as s:
    sisu = s.read()
    print("Tehti", sisu.count("Hello"), "asendamist.")
with open(f2, "w") as v, open (f1) as s:
    v.write(s.read().replace("Hello", "Tere"))

    



