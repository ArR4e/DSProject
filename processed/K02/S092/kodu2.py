pikkus = int(input("Sisestage liini pikkus: "))
kaugus = int(input("Sisestage maksimaalakugus: "))

postid = int(pikkus / kaugus)

if pikkus < kaugus:
    print(2)
elif (pikkus % kaugus) == 0:
    print(postid + 1)
else:
    print(postid + 2)