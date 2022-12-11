aastatulu = float(input("Sisesta aastatulu: "))

if 0 <= aastatulu < 6000:
    tulu = aastatulu
    maksuvaba_tulu = "Maksuvaba tulu on " + str(tulu) + " eurot."
elif aastatulu >= 6000 and aastatulu <= 14400:
    tuluilma = aastatulu - 6000
    tulu= round(tuluilma, 2)
    maksuvaba_tulu = "Maksuvaba tulu on " + str(tulu) + " eurot."
elif aastatulu >= 14400 and aastatulu <= 25200:
    tuluilma = 6000 - 6000 / 10800 * (aastatulu - 14400)
    tulu= round(tuluilma, 2)
    maksuvaba_tulu = "Maksuvaba tulu on " + str(tulu) + " eurot."
elif aastatulu < 0:
    maksuvaba_tulu = "Mitte arvestatav."
else:
    tulu = 0

print(maksuvaba_tulu)