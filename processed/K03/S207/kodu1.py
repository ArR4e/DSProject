sissetulek = float(input("Sisesta aastatulu: "))

if sissetulek >= 0 and sissetulek < 6000:
    maksuvaba = sissetulek
elif sissetulek >= 6000 and sissetulek <=14400:
    maksuvaba = 6000
elif sissetulek > 14400 and sissetulek < 25200:
    maksuvaba = 6000 - 6000 / 10800 * (sissetulek - 14400)
elif sissetulek >= 25200:
    maksuvaba = 0
    
print(f"Maksuvaba tulu on {round(maksuvaba, 2)} eurot.")