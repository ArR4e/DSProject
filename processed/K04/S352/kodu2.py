c=299792.458
def summa(u,v):
    return (u+v)/(1+(u*v)/c**2)
    
i=float(input("I keha v: "))
ii=float(input("II keha v: "))
iii=float(input("III keha v: "))
iv=float(input("IV keha v: "))

print("Kiirustensumma: ",summa(summa(summa(i,ii),iii),iv))