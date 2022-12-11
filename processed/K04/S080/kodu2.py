c=299792.458
d = 0
def summa(u,v):
    u=(u+v)/(1+((u*v)/(c**2)))
    return u
#def summa(v,x):
    #v=(v+x)/(1+((v*x)/(c**2)))
    #return v

    
    
u=float(input('Esimese keha kiirus vaatleja suhtes on: '))
v = float(input('Teise keha kiirus esimese kega suhtes on: '))
x = float(input('Kolmanda keha kiirus teise kega suhtes on: '))
y = float(input('Neljanda keha kiirus kolmanda kega suhtes on: '))
uv=(summa(u,v))
xy=(summa(x,y))
a = uv
b = xy
print("Kiiruste summa on",summa(a,b),"km/s")