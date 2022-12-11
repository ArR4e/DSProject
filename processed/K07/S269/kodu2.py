f = open("taksohinnad.txt", encoding="utf-8")
d = float(input("Sisesta tee pikkus kilomeetrites: "))
takso = ""
hind = float('inf')
for rida in f:
    t = rida.strip().split(",")
    if float(t[1]) + d*float(t[2]) < hind:
        takso = t[0]
        hind = float(t[1]) + d*float(t[2])

print("Kõige odavam on " + takso + ".")
    