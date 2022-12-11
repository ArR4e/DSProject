u = float (input("Sisestage esimene kiirus: "))
v = float(input("Sisestage teine kiirus: "))
x = float(input("Sisestage kolmas kiirus: "))
y = float(input("Sisestage neljas kiirus: "))


def summa (u, v):
    return (u + v)/(1 + ((u*v)/299792.458**2))

uvsumma = summa (u, v)
uvxsumma = summa (uvsumma, x)
uvxysumma= summa (uvxsumma, y)

print ("Kiiruste summa on " + str(uvxysumma) + " km/s.")