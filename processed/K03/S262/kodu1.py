aastatulu = float(input("Sisesta aastatulu: "))
maksuvaba = 0
if aastatulu >= 25200 :
    maksuvaba = 0
elif aastatulu >= 14400:
    maksuvaba = round(6000 - 6000 / 10800 * (aastatulu - 14400), 2)
elif aastatulu <= 6000:
    maksuvaba = aastatulu
else:
    maksuvaba = 6000
print("Maksuvaba tulu on",str(maksuvaba),"eurot.")