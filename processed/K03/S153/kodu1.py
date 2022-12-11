aastatulu = float(input("Sisesta aastatulu: "))
aastatulu = abs(aastatulu)
maksuvaba_tulu = ""

if aastatulu <= 6000:
    maksuvaba_tulu = aastatulu
elif 6000 <= aastatulu <= 14400:
    maksuvaba_tulu = 6000
elif 14400 <= aastatulu <= 25200:
    maksuvaba_tulu = (6000 - 6000 / 10800 * (aastatulu - 14400))
elif aastatulu >= 25200:
    maksuvaba_tulu = 0
    
maksuvaba_tulu = round(float(maksuvaba_tulu), 2)

print("Maksuvaba tulu on " + str(maksuvaba_tulu))