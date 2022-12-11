def summa(u,v):
    c=299792.458
    return (u+v)/(1+(u*v)/(c**2))
kiirus1=float(input("Sisesta esimese keha kiirus: "))
kiirus2=float(input("Sisesta teise keha kiirus: "))
kiirus3=float(input("Sisesta kolmanda keha kiirus: "))
kiirus4=float(input("Sisesta neljanda keha kiirus: "))

kiiruste_summa=summa(summa(summa(kiirus1,kiirus2),kiirus3),kiirus4)
print("Kiiruste summa on",kiiruste_summa)
