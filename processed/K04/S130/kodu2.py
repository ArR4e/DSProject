# teooria valem : (u+v)/(1+(u*v)/c**2)
c = 299792.458 

u = float(input("Esimese keha kiirus vaatleja suhtes on: ")) 
v = float(input("Teise keha kiirus esimese keha suhtes on: ")) 
x = float(input("Kolmande keha kiirus teise keha suhtes on: ")) 
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: ")) 

def summa(u,v):
    summa = u+v
    jagatis = 1 + (u*v)/c**2
    teoreem1 = summa/jagatis
    kolmas = teoreem1+x
    kolmas_jagatis= 1 + (teoreem1*x)/c**2
    teoreem2 = kolmas/kolmas_jagatis
    neljas = teoreem2+y
    neljas_jagatis = 1 + (teoreem2*y)/c**2
    teoreem3 = neljas/neljas_jagatis
    return teoreem3
 
print("Kiiruste summa on", summa(u, v) , "km/h")