aastatulu = float(input("Sisesta aastatulu: "))
maksuvaba_tulu = 0
if aastatulu < 6000:
    maksuvaba_tulu = aastatulu
elif aastatulu >= 6000 and aastatulu < 14400:
    maksuvaba_tulu = 6000
elif aastatulu >= 14400 and aastatulu < 25200:
    maksuvaba_tulu = 6000 - 6000 / 10800 * (aastatulu - 14400)
elif aastatulu > 25200:
    maksuvaba_tulu = 0

    
print("Maksuvaba tulu on", round(maksuvaba_tulu, 2), "eurot.")
    
