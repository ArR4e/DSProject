# 1. Maksuvaba tulu / RP

tulu = float(input("Sisesta aastatulu: "))

if tulu <= 6000:
    maksuvaba = tulu
elif tulu > 6000 and tulu <= 14400:
    maksuvaba = 6000
elif tulu < 25200:
    maksuvaba = 6000 - 6000 / 10800 * (tulu - 14400)
else:
    maksuvaba = 0
    
print("Maksuvaba tulu on " + str(round(maksuvaba, 2)), "eurot.")