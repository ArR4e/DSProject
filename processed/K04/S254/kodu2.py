u=input("Sisend1")
v=input("Sisend2")
x=input("Sisend3")
y=input("Sisend4")
def summa(u,v):
    c=299792.458
    u=float(u)
    v=float(v)
    return (u+v)/(1+((u*v)/(c*c)))

print(summa(y,summa(x,summa(u,v))))