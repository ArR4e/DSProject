from math import ceil
liini_pikkus = int(input("Sisesta liini pikkus täismeetrites: "))
max_kaugus = int(input("Sisesta postide maksimaalne kaugus täismeetrites: "))

postide_arv = ceil(liini_pikkus/max_kaugus) + 1
print("Kokku on " + str(postide_arv) +
      " posti vahekaugusega " + str(liini_pikkus/(postide_arv-1)))

#print(postide_arv)