aastatulu = float(input("Sisesta aastatulu: "))

if aastatulu <= 6000:
    maksuvabatulu = aastatulu
elif 6000 < aastatulu <= 14400:
    maksuvabatulu = 6000
elif 14400 < aastatulu <= 25200:
    maksuvabatulu = 6000 - 6000 / 10800 * (aastatulu - 14400)
else:
    maksuvabatulu = 0
    
maksuvabatulu = round(maksuvabatulu, 2)
    
print("Maksuvaba tulu on", maksuvabatulu, "eurot.")
