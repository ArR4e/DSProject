u = float(input("sisestage esimene kiirus: "))
v = float(input("sisestage teine kiirus: "))
x = float(input("sisestage kolmas kiirus: "))
y = float(input("sisestage neljas kiirus: "))
c = 299792.458

def summa(u, v):
    s = (u+v)/(1+((u*v)/c**2))
    s1 = (s+x)/(1+((s*x)/c**2))
    su = (s1+y)/(1+((s1*y)/c**2))
    return su

print(f"kiiruste summa on {summa(u, v)} km/h")   
    