liini_pikkus = int(input("Sisesta liini pikkus: "))
max_kaugus = int(input("Sisesta postide vaheline maksimaalne kaugus: "))
if liini_pikkus % max_kaugus == 0:
    postide_arv = int(liini_pikkus / max_kaugus) + 1
else:
    postide_arv = int(liini_pikkus / max_kaugus) + 2
print(postide_arv)