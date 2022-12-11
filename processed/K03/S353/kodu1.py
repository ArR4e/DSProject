aastatulu = float(input("Palun sisetage oma aastatulu (mittenegatiivse arvuna, tühikuta) :"))
if aastatulu <= 6000:
    maksuvaba = aastatulu
elif aastatulu <= 25_200 :
    maksuvaba = 6000 - 6000 / 10_800 * (aastatulu - 14_400)
else:
    maksuvaba = 0
print("Teie maksuvaba tulu on :", round(maksuvaba, 2), '€ aastas.')