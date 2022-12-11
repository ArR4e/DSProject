pikkus = int(input("Sisesta liini pikkus: "))
max_kaugus = int(input("Sisesta kahe posti maksimaalkaugus: "))



if pikkus == max_kaugus:
    postide_arv = pikkus/max_kaugus + 1
elif max_kaugus == 1:
    postide_arv = pikkus + 1
else:
    postide_arv = pikkus/max_kaugus + 2


print(int(postide_arv))