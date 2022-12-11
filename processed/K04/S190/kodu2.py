c = 299792458/1000
def summa(a,b):
    return float((a+b)/(1+(a*b/c**2)))
    

u = float(input("Sisesta esimese keha liikumiskiirus: "))
v = float(input("Sisesta teise keha liikumiskiirus: "))
x = float(input("Sisesta kolmanda keha liikumiskiirus: "))
y = float(input("Sisesta neljanda keha liikumiskiirus: "))



esimene = summa(u,v)
teine = summa(esimene,x)
kolmas = summa(teine,y)
print(str(kolmas)+" km/s")
