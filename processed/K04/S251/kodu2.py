def summa(a,b):
    c = 299792.458
    return (a+b) / ( 1 + ( a * b ) / c**2)

kiirus1 = float(input("Sisestage esimene kiirus: "))
kiirus2 = float(input("Sisestage teine kiirus: "))
kiirus3 = float(input("Sisestage kolmas kiirus: "))
kiirus4 = float(input("Sisestage neljas kiirus: "))

print("Kiiruste summa on " + str(summa(kiirus4, summa(kiirus3, summa(kiirus2, kiirus1)))))