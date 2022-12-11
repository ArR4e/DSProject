#Einsteini erirelatiivsusteooria

def summa(u,v):
    c= 299792.458
    kiirus= (u+v)/(1+((u*v)/c**2))
    return kiirus

u= float(input('Sisesta esimese keha kiirus: '))
v= float(input('Sisesta teise keha kiirus: '))
kiirus1= summa(u,v)
x= float(input('Sisesta kolmanda keha kiirus: '))
kiirus2= summa(kiirus1,x)
y= float(input('Sisesta neljanda keha kiirus: '))

print('Kiiruste summa on',summa(kiirus2,y),'km/s')