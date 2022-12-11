import math

tekst1 = input("Palun sisesta elektriliini pikkus meetrites: ")
arv1 = float(tekst1)

tekst2 = input("Palun sisesta elektriliini postide maksimaalkaugus meetrites: ")
arv2 = float(tekst2)

postid = math.ceil((arv1 / arv2) + 1)

if arv1 < arv2:
    print("Elektriliini postide arv on: 2")
else:
    print("Elektriliini postide arv on: " + str(postid))
