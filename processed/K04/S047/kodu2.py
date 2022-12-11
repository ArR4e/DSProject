def summa(u, v):
    
    c=299792.458
    a=((u+v)/(1+u*v/c**2))
    global g, f
    b=((a+g)/(1+a*g/c**2))
    return(round((b+f)/(1+b*f/c**2),4))

a=int(input("sisesta esimese keha kiirus: " ))
b=int(input("sisesta teise keha kiirus: " ))
g=int(input("sisesta kolmanda keha kiirus: " ))
f=int(input("sisesta neljanda keha kiirus: " ))

print("vaatleja jaoks liiga neljas keha kiirusega", summa(a, b))