def summa(u, v):
    return ((u+v)/(1+(u*v)/299792.458**2))

e = float(input("Palun sisestage esimese keha kiirus: "))
t = float(input("Palun sisestage teise keha kiirus: "))
k = float(input("Palun sisestage kolmanda keha kiirus: "))
n = float(input("Palun sisestage neljanda keha kiirus: "))
s1 = summa(e, t)
s2 = summa(s1, k)
s3 = summa(s2, n)

print("Kiiruste summa on: "+str(s3)+".")