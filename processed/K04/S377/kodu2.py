#mirjampirn

def sum(u,v):
    c=299792.458
    kogukiirus=(u+v)/(1+(u*v)/(c*c))
    return kogukiirus

kiirus1=float(input("Esimese kiirus (km/s): "))
kiirus2=float(input("Teise kiirus (km/s): "))
kiirus3=float(input("Kolmanda kiirus (km/s): "))
kiirus4=float(input("Neljanda kiirus (km/s): "))

kiirus12=sum(kiirus1,kiirus2)
kiirus123=sum(kiirus12,kiirus3)
kiirus1234=sum(kiirus123,kiirus4)
print("Kiiruste summa on "+str(kiirus1234)+" km/s")