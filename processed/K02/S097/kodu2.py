a=int(input("Liini pikkus meetrites: "))
b=int(input("Postidevaheline maksimaalkaugus meetrites: "))


if a%b > 0 and a/b >= 1:
    arv=str(a // b + 2)
if a%b == 0 and a/b >= 1:
    arv = str(a // b + 1)
if a/b <= 1:
    arv = str(2)

print("Liini ehitamiseks on vaja minimaalselt " + arv + " posti.")