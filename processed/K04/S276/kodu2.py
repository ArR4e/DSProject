u=int(input("Esimese keha kiirus vaatleja suhtes on: "))
v=int(input("Teise keha kiirus esimese keha suhtes on: "))
def summa (u, v):
   return(round((u+v)/(1+u*v/299792.458**2), 2))