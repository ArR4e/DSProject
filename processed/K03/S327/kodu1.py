aastatulu = float(input("Sisesta aastatulu: "))
maksuvaba_tulu = 6000
if aastatulu <= 6000:
    maksuvaba_tulu = aastatulu
elif aastatulu > 6000 and aastatulu < 14400:
    maksuvaba_tulu = 6000
elif aastatulu >= 14400 and aastatulu < 25200 :
    maksuvaba_tulu = round(6000 - 6000 / 10800 * (aastatulu - 14400), 2)
else:
    maksuvaba_tulu = 0
print("Maksuvaba tulu on " + str(maksuvaba_tulu) + " eurot.")