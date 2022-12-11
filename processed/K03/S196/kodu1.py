tulu = float(input("Sisesta aastatulu: "))
if tulu > 25200:
    print("Maksuvaba tulu on 0 eurot.")
elif tulu <= 25200 and tulu > 14400:
    mvtulu = 6000 - 6000 / 10800 * (tulu - 14400)
    mvtulu = round(mvtulu, 2)
    print("Maksuvaba tulu on " + str(mvtulu) + " eurot.")
elif tulu <= 14400 and tulu > 6000:
    print("Maksuvaba tulu on 6000.00 eurot.")
elif tulu <= 6000 and tulu >= 0:
    tulu = round(tulu, 2)
    print("Maksuvaba tulu on " + str(tulu) + " eurot.")
else:
    print("Tulu ei saa olla negatiivne")