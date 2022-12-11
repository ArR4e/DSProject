tulu = float(input("Sisestage aastatulu: "))

if tulu <= 6000:
    maksuvaba = round(tulu, 2)
    
elif tulu <= 14400:
    maksuvaba = 6000
    
elif tulu <= 25200:
    maksuvaba = round(6000 - 6000 / 10800 * (tulu - 14400), 2)
    
else:
    maksuvaba = 0
    
print("Maksuvaba tulu on ", str(maksuvaba), " eurot.")