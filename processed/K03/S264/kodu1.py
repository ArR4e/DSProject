aastatulu = float(input("Sisestage aastatulu: "))

if aastatulu < 0:
    print("Arv peab olema positiivne")
elif aastatulu < 6000:
    maksuvaba_tulu = aastatulu
elif aastatulu <= 14400:
    maksuvaba_tulu = 6000
elif aastatulu <= 25200:
    maksuvaba_tulu = 6000 - 6000 / 10800 * (aastatulu - 14400)
if aastatulu > 25200:
    maksuvaba_tulu = 0

print("Maksuvaba tulu on", round(maksuvaba_tulu, 2), "eurot.")
    
