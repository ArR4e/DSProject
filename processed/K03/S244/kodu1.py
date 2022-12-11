aasta_tulu = abs(float(input("Sisesta aastatulu: ")))
if aasta_tulu <= 6000:
    print("Maksuvaba tulu on " + str(aasta_tulu) + " eurot.")
if 6000 < aasta_tulu < 14400:
    print("Maksuvaba tulu on " + str(6000) + " eurot.")
if 14400 <= aasta_tulu <= 25200:
    print("Maksuvaba tulu on " + str(round(6000 - 6000 / 10800 * (aasta_tulu - 14400), 2)) + " eurot.")
if aasta_tulu > 25200:
    print("Maksuvaba tulu on " + str(0) + " eurot.")
