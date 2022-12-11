x = int(input("Sisesta naturaalarv: "))
natarvudesumma = 0
natarvuderuutsumma = 0
while x > 0:
    natarvuderuutsumma += x**2
    natarvudesumma += x
    x -= 1
    if x == 0:
        natarvudesummaruut = natarvudesumma**2
erinevus = natarvudesummaruut - natarvuderuutsumma
print(natarvudesummaruut)
print(erinevus)