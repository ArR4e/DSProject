aastatulu = float(input("Sisesta aastatulu: "))
if aastatulu < 0:
    aastatulu = -aastatulu
    
if aastatulu < 6000:
    maksuvaba_tulu = aastatulu
elif aastatulu == 6000 or aastatulu < 14400:
    maksuvaba_tulu = 6000
elif aastatulu == 14400 or aastatulu < 25200:
    maksuvaba_tulu = 6000-6000 / 10800 * (aastatulu - 14400)
else:
    maksuvaba_tulu = 0
    
print("Maksuvaba tulu on " + str(round(maksuvaba_tulu, 2)) + " eurot.")