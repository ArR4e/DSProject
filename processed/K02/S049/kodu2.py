#postid asetsevad maksimaalkaugustel üksteisest
a = int(input("Sisestage liini pikkus: "))
b = int(input("Sisestage postide maksimaalkaugus: "))
c = (float(a / b))
print(input("Minimaalne postide arv: " + str(c)))

#postid asetsevad lähemal kui maksimaalkaugus
a = int(input("Sisestage liini pikkus: "))
b = int(input("Sisestage postide maksimaalkaugus: "))
c = (float(a / b * 2))
print(input("Postide arv: " + str(c)))

#liini pikkus on väiksem kui maksimaalkaugus
a = int(input("Sisestage liini pikkus: "))
b = int(input("Sisestage postide maksimaalkaugus: "))
c = (float(a / b))
if a <= b:
    print("Ei ole võimalik teostada")
elif a > b:
    print(float(a /b))
