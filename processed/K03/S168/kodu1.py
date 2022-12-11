while True:
    try:
        aastatulu = float(input("Sisesta aastatulu: "))
        if aastatulu < 0:
            raise Exception
        break
    except:
        print("Aastatulu peab olema mittenegatiivne ujumkomaarv.")
if aastatulu < 6000:
    maksuvaba_tulu = aastatulu
elif 6000 <= aastatulu < 14_400:
    maksuvaba_tulu = 6000
elif 14_400 <= aastatulu < 25_200:
    maksuvaba_tulu = 6000 - 6000 / 10_800 * (aastatulu - 14_400)
else:
    maksuvaba_tulu = 0
print("Teie maksuvaba tulu on:", round(maksuvaba_tulu), "eurot.")