suurimpikkus = int(input("Sisesta liini pikkus "))
postidepikkus = int(input("Sisesta postide vahede pikkus "))

x = 2 + ((suurimpikkus - 1) // postidepikkus)
print("Postide arv on " + str(x))