u= float(input("keha kiirus"))
v= float(input("keha kiirus"))
x= float(input("keha kiirus"))
y= float(input("keha kiirus"))
c= 299792.458

def summa(a, b):
    global kokku
    kokku=((a+b)/(1+((a*b)/c**2)))
    
    
    
    return kokku

summa(0, u)
summa(kokku, v)
summa(kokku, x)
summa(kokku, y)

print("Kiiruste summa on " + str(kokku) + " km/s")
    
    

