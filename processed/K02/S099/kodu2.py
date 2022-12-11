from math import ceil

pikkus = int(input("Sisesta liini pikkus: "))
vahe = int(input("Sisesta postide maksimaalkaugus: "))

postide_arv = ceil(pikkus / vahe) + 1
#print("Liini ehitamiseks on vaja vähemalt " + str(postide_arv) + " posti.")
print(str(postide_arv))