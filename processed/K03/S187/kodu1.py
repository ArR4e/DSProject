tulu = float(input("Mul on vaja see proge kodutöö ära teha, aita välja ja sisesta palun oma aastane tulu: "))

if tulu <= 6000:
    maksuvaba = tulu
elif tulu <= 14400:
    maksuvaba = 6000
elif tulu <= 25200:
    maksuvaba = 6000 - 6000/10800 * (tulu - 14400)
else:
    maksuvaba = 0

maksuvaba = round(maksuvaba, 2)
print("Suured tänud, mees, sinu maksuvaba tulu on", maksuvaba, "eurot.")