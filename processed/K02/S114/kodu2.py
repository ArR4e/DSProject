pikkus = int(input("Sisesta liini pikkus: "))
kaugus = int(input("Sisesta postide kaugus: "))
postide_arv = 2 #alguses ja lõpus olemas 1
if pikkus <= kaugus:
    print("Vaja läheb "+str(postide_arv)+" posti")
elif pikkus/kaugus == postide_arv:
    postide_arv += int(pikkus/kaugus)-1
    print("Vaja läheb "+str(postide_arv)+" posti")
else:
    postide_arv += int(pikkus/kaugus)
    print("Vaja läheb "+str(postide_arv)+" posti")
