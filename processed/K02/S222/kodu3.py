tapitahed = ["Ö","Ä","Ü","Õ"]
tahed = ["o","a","u","o"]

eesnimi = input("Sisesta eesnimi: ").lower()
perenimi = input("Sisesta perenimi: ").lower()

a = 0
pikkus1 = len(eesnimi)
pikkus2 = len(perenimi)

while pikkus1 > a:
    if eesnimi[a].upper() in tapitahed:
        eesnimi = eesnimi.replace(eesnimi[a],tahed[tapitahed.index(eesnimi[a].upper())])
    a += 1
    
a = 0

while pikkus2 > a:
    if perenimi[a].upper() in tapitahed:
        perenimi = perenimi.replace(perenimi[a],tahed[tapitahed.index(perenimi[a].upper())])
    a += 1

print(eesnimi+"."+perenimi)