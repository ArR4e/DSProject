f = open("taksohinnad.txt", encoding = "UTF-8")
loe = f.read()
print(loe)

teepikkus = (input("Sisesta tee pikkus kilomeetrites: "))

hind = stardihind + (teepikkus * km_tasu)


print("Kõige odavam on " )
f.close()