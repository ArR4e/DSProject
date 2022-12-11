from math import ceil
liini_pikkus = int(input("Sisestage elektriliini pikkus: "))
postide_vahe = int(input("Sisestage postide vaheline maksimaalne kaugus: "))
poste = ceil(float(liini_pikkus/postide_vahe)) + 1
print(int(poste))