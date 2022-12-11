def summa(u,v):
    return float((float(u)+float(v))/(1+((float(u)*float(v))/299792.458**2)))
print(summa(summa(summa(input("Esimene: "), input("Teine: ")), input("Kolmas: ")), input("Neljas: ")))