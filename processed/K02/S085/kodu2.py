a = int(input("Palun sisestage liini pikkus:"))
b = int(input("Palun sisestage postidevaheline maksimaalne kaugus:"))
postide_arv = a // b + 2
postid = a // b + 1
if a % b:
    print(postide_arv)
else:
    print(postid)
