from math import ceil
liini_pikkus=int(input("Sisesta liinipikkus täisarvuna: "))
postide_kaugus=int(input("Sisesta maksimaalne postide vaheline kaugus täisarvuna: "))
mitu_posti=ceil((liini_pikkus/postide_kaugus)+1)
print("Liini ehitamiseks läheb vaja "+ str(mitu_posti)+" posti.")