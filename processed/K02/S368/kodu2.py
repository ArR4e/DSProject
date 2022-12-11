pikkus = int(input("Liini Pikkus: "))
pVahe = int(input("Max postide vahe: "))

if (pikkus % pVahe == 0):
    print(pikkus//pVahe +1)
else:
 print(pikkus // pVahe + 2 ) 