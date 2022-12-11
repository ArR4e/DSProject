kiirus=0
b=1
c=299792.458
def summa(u,v):
    kiirus=(u+v)/(1+u*v/c**2)
    return kiirus
v=float(input(str(b)+'. keha kiirus vaatleja suhtes on: ')) 
while True:
    b+=1
    try:
        u=float(input(str(b)+'. keha kiirus '+str(b-1)+ '. keha suhtes on: '))
    except:
        break
    v=summa(u,v)
print(v)
    