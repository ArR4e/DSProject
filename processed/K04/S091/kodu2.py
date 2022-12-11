c = 299792.458
x = 0
def summa(u, v):
    global x
    x = (u + v)/(1+(u*v)/(c**2))
    return x
    

for i in range(0,3):
    if i == 0:
        u = float(input("Esimene kiirus: "))
        v = float(input("Teine kiirus: "))
        summa(u,v)
        u = x
    elif i == 1:
        v = float(input("Kolmas kiirus: "))
        summa(u,v)
        u = x
    else:
        v = float(input("Neljas kiirus: "))
        summa(u,v)
        u = x
        
print(round(u, 5))
        
