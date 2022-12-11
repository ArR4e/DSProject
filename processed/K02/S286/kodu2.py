import math
liinipikkus = int(input("Sisesta elektriliini pikkus: "))
postidevahe = int(input("Sisesta postidevaheline kaugus: "))
postidearv = (math.ceil(liinipikkus/postidevahe)+1)
print(postidearv)