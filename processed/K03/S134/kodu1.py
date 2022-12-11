aastatulu = float(input("Sisesta aastatulu: "))
if aastatulu <= 6000:
    b = round(aastatulu, 2)
    print("Maksuvaba tulu on " + str(b) + " eurot.")
elif aastatulu >= 6000 and aastatulu <= 14400:
    print("Maksuvaba tulu on 6000 eurot.")
elif aastatulu >= 14400 and aastatulu <= 25200:
    a = round(6000 - 6000 / 10800 * (float(aastatulu) - 14400), 2)
    print("Maksuvaba tulu on " + str(a) + " eurot.")
elif aastatulu > 25200:
    print("Maksuvaba tulu on 0 eurot.")