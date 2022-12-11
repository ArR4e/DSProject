u = float(input("u: "))
v = float(input("v: "))
x = float(input("x: "))
y = float(input("y: "))

def summa(u,v):
    c = 299792.458
    sumUV = float(float(u+v)/(1+float(float(u*v)/c**2)))
    return sumUV

sum1 = summa(u,v)
sum2 = summa (sum1,x)
sum3 = summa (sum2,y)
print (sum1)
print (sum2)
print ("summa="+ str(sum3))