def summa(u,v):
    return((u+v)/(1+(u*v/(299792.458**2))))
u=float(input("esimese keha kiirus on "))
v=float(input("teise keha kiirus on "))
x=float(input("kolmanda keha kiirus on "))
y=float(input("neljanda keha kiirus on "))
kogusumma=summa(u,v)
kogusumma=summa(kogusumma,x)
kogusumma=summa(kogusumma,y)
print("Kiiruste summa on",kogusumma,"m/s")
