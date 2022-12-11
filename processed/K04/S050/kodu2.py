
def summa(u,v):
    c=299792.458
    return (u+v)/(1+((u*v)/c**2))
k1=float(input('Sisesta esimese keha kiirus: '))
k2=float(input('Sisesta teise keha kiirus: '))
k3=float(input('Sisesta kolmanda keha kiirus: '))
k4=float(input('Sisesta neljanda keha kiirus: '))

ksumma=summa(summa(summa(k1,k2),k3),k4)

print('Kiiruste summa on', ksumma)