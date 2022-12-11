# from scipy import constants
# ei osanud Scipy-t installeerida ja c täpne väärtus jäi saamata
u = float(input("Esimese keha kiirus, km/s: "))
v = float(input("Teise keha kiirus, km/s: "))
x = float(input("Kolmanda keha kiirus, km/s: "))
y = float(input("Neljanda keha kiirus, km/s: "))
def summa(u, v):
    return (u + v)/(1+u*v/299792.458**2)
summa1 = summa(u,v)
summa2 = summa(summa1,x)
summa3 = summa(summa2,y)
print("")
print("Kehade summaarne kiirus on", round(summa3, 2), "km/s")