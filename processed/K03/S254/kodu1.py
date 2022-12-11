#Maksuvaba tulu

aastatulu = abs(float(input("Sisestage oma teie aastatulu (eur): ")))
arvutus=0

if aastatulu <= 6000:
    arvutus=aastatulu
elif aastatulu > 6000 and aastatulu <= 14400:
    arvutus=6000
elif aastatulu > 14400 and aastatulu <= 25200:
    arvutus=6000 - 6000 / 10800 * (aastatulu - 14400)
else:
    arvutus=0




maksuvabatulu=round(arvutus,2)

print("Maksuvaba tulu on " + str(maksuvabatulu) + " eurot.")