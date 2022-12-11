aastatulu = int(input("Sisesta aastatulu: "))
if (aastatulu) < 6000:
   print("Maksuvaba tulu on: " + aastatulu + " eurot.")

if 6000 <= aastatulu and aastatulu <= 14400:
    print("Maksuvaba tulu on: 6000 eurot.")

if 14400 < aastatulu and aastatulu <= 25200:
    maksuvaba_tulu = 6000-6000/10800*(aastatulu - 14400)
    print("Maksuvaba tulu on: " + str(round(maksuvaba_tulu, 2)) + " eurot.")

if aastatulu > 25200:
    print("Maksuvaba tulu on 0 eurot.")



