import math
pikkus = int(input("Sisesta liinipikkus täisarvuna (m): "))
postid = int(input("Sisesta maksimaalne postidevaheline kaugus (m): "))
print(math.ceil(pikkus/postid ) + 1)