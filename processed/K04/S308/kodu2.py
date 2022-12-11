u=float(input('Sisestage esimese keha kiirus vaatleja suhtes: '))
v=float(input('Sisestage teise keha kiirus esimese keha suhtes: '))
x=float(input('Sisestage kolmanda keha kiirus teise keha suhtes: '))
y=float(input('Sisestage neljanda keha kiirus kolmanda keha suhtes: '))
c=29979245**8
def summa(u,v):
    kiirus1=(u+v)/(1+((u*v)/c**2))
    kiirus=kiirus1
    
    kiirus2=(v+x)/(1+((v*x)/c**2))
    kiirus+=kiirus2
    
    kiirus3=(x+y)/(1+((x*y)/c**2))
    kiirus+=kiirus3
    
    return(kiirus)
summa(u,v)
print(summa(u,v))