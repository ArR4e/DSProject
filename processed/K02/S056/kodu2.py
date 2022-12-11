from math import ceil
liini_pikkus = input("Mitu meetrit liini on vaja ehitada: ")
maksimaalne_kaugus = input("Mis on postide maksimaalne kaugus üksteisest: ")
postide_arv = ceil(int(liini_pikkus) / int(maksimaalne_kaugus)) + 1
print(postide_arv)


