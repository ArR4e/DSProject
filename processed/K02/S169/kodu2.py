import math
liin = int(input("Sisesta liini pikkus: "))
vahed= int(input("Sisesta max postide vaheline kaugus: "))

if liin > vahed:
    postid = math.ceil(liin/vahed) + 1
    print("Poste on vaja " + str(postid))
if liin <= vahed:
    postid = 2
    print("Poste on vaja " + str(postid))