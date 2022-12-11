tulu = float(input("Sisestage aastatulu: "))

if tulu < 6000:
    print("Maksuvaba tulu on " + str(round(tulu, 2)) + " eurot.")
elif 6000 <= tulu < 14400:
    print("Maksuvaba tulu on 6000 eurot.")
elif 14400 <= tulu < 25200:
    maksuvaba = round((6000 - 6000 / 10800 * (tulu - 14400)), 2)
    print("Maksuvaba tulu on " + str(maksuvaba) + " eurot")
else:
    print("Maksuvaba tulu on 0 eurot.")