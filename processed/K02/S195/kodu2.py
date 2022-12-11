import math

liinpikk = float(input("Palun sisesta kogu liinipikkus: "))
postmax = float(input("Palun sisesta kahe posti vaheline maksimaalkaugus: "))

a = 1 + liinpikk/postmax
postarv = math.ceil(a)

print("Minimaalne arv poste liini ehitamiseks on ", postarv)