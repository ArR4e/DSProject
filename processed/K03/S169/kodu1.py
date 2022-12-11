tulu = float(input("Sisesta aastatulu: "))

if tulu >= 25200:
    maksuvaba = 0
if tulu > 14400 and tulu < 25200:
    maksuvaba = 6000 - 6000 / 10800 * (tulu -14400)
if tulu <= 14400:
    if tulu > 6000:
        maksuvaba = 6000
    else:
        maksuvaba = tulu
    
print("Maksuvaba tulu on",round(maksuvaba,2), "eurot")