def summa(u,v):
    c = 299792.458 # km/s
    lugeja = u+v
    nimetaja = 1+((u*v)/(c**2))
    valem = lugeja / nimetaja
    return valem
I = float(input("Esimese keha kiirus: "))
II = float(input("Teise keha kiirus: "))
III = float(input("Kolmanda keha kiirus: "))
IV = float(input("Neljanda keha kiirus: "))
I_ja_II_tulemus = summa(I,II)
II_ja_III_tulemus = summa(I_ja_II_tulemus, III)
III_ja_IV_tulemus = summa(II_ja_III_tulemus, IV)
tulemus = III_ja_IV_tulemus
print(tulemus)
