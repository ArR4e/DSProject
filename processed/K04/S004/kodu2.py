c=299792.458
def summa(u,v):
    return((u+v)/(1+((u*v)/c**2)))
kiirus1=float(input("1.kiirus"))
kiirus2=float(input("2.kiirus"))
kiirus3=float(input("3.kiirus"))
kiirus4=float(input("4.kiirus"))
a=summa(kiirus1,kiirus2)
b=summa(a,kiirus3)
print(summa(b,kiirus4))