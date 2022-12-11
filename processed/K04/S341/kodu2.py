n= float(input("Esimese keha kiirus vaatleja suhtes on:"))
m= float(input("Teise keha kiirus esimese keha suhtes:"))
e= float(input("Kolmanda keha kiirus esimese keha suhtes:"))
f= float(input("Neljanda keha kiirus esimese keha suhtes: "))
def summa(u,v,x,y):
    global n
    global m
    global e
    global f
    n = u
    m = v
    e = x
    f = y
    c= 299792.458
    d = (u + v)/(1 + (u * v)/(c**2))
    g = (d + x)/1 +(d * x)/(c**2)
    h = (g + f)/1 + (g * f)/(c**2)
    return (h)
summa(n,m, e, f)
print("Kiiruste summa on ", summa(n,m, e,f) )


    
    