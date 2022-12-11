#Einsteini erirealatiivsusteooria
u=float(input("Mis on esimese keha kiirus?"))
v=float(input("Mis on teise keha kiirus?"))
x=float(input("Mis on kolmanda keha kiirus?"))
y=float(input("Mis on neljanda keha kiirus?"))
# valem = (u+v)/(1+(u*v)/c**2)
c=299792.458
def summa(u, v):
    sum= (u + v)/(1+(u*v)/c**2)
    return sum



e = summa(u, v)
t = summa(e, x)
k = summa(t, y)
print(k)