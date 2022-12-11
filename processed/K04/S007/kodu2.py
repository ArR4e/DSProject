#u = 1. keha kiirus vaatleja suhtes
#v = 2. keha kiirus 1. keha suhtes



def summa(u, v):
    c=299792.458 #km/s
    #kiirus= 2. keha kiirus vaatleja suhtes
    kiirus = (u+v) / (1+(u*v)/(c*c))
    return kiirus

    


u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
         
         
print("Kiiruste summa on ",summa(summa(summa(u, v),x),y), "km/s")
