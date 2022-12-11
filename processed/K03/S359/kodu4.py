#failinimi= input("Sisestage faili nimi: ")
a=open("kinganumbrid.txt", "r")
pikkus=0
for f in a:
    try:
        f= float(f.strip())
        pikkus =round(2/3 * (f - 2))
        print(pikkus)
    except:
        print("Vigane sisend.")