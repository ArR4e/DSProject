c=float(299792.458)

def summa(u, v):
    return(((u+v) / (1+ (u*v) / (c**2))))

u=input("Sisestage objekti u kiirus vaatleja suhtes: ")
if u.find("."):
    u=float(u)
else:
    u=int(u)
v=input("Sisestage objekti v kiirus u suhtes: ")
if v.find("."):
    v=float(v)
else:
    v=int(v)    
x=input("Sisestage objekti x kiirus v suhtes: ")
if x.find("."):
    x=float(x)
else:
    x=int(x)    
y=input("Sisestage objekti y kiirus x suhtes: ")
if y.find("."):
    y=float(y)
else:
    y=int(y)

summa1=summa(u, v)
summa2=summa(summa1, x)
summa3=summa(summa2, y)
    

print("Kiiruste summa on", summa3, "km/s")



