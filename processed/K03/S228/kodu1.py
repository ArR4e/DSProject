aastatulu = float(input("Sisesta aastatulu eurodes: "))
maksuvaba_arvutusk2ik = round(6000 - 6000 / 10800 * (aastatulu - 14400), 2)

if aastatulu < 6000:
    print("Maksuvaba tulu on " + str(aastatulu) + " eurot.")
elif 6000 <= aastatulu < 14400:
    print("Maksuvaba tulu on 6000.00 eurot.")
elif 14400 <= aastatulu < 25200:
    print("Maksuvaba tulu on " + str(maksuvaba_arvutusk2ik) + " eurot.")
elif aastatulu >= 25200:
    print("Maksuvaba tulu on 0 eurot.")
else:
    print("Viga.")