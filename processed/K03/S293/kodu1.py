tulu=float(input("Sisesta siia oma aastane tulu: "))

if tulu>=0 and tulu<6000:
    print("Aastane maksuvaba tulu on", str(round(tulu, 2)), "eurot")
elif tulu>=6000 and tulu<14400:
    print("Aastane maksuvaba tulu on 6000.0 eurot")
elif tulu>=14400 and tulu<25200:
    print("Aastane maksuvaba tulu on", str(round(6000 - 6000 / 10800 * (tulu - 14400), 2)), "eurot")
elif tulu>=25200:
    print("Aastane maksuvaba tulu on 0 eurot")