aastatulu = float(input("sisestage aastatulu eurodes: "))
if aastatulu < 6000:
    print("maksuvabatulu on võrdne aastatuluga")
elif aastatulu < 14400:
    print("maksuvaba tulu on 6000 eurot aastas")
elif aastatulu < 25200:
    maksuvaba_tulu = round(6000 - 6000 / 10800 * (aastatulu - 14400), 2)
    print("maksuvaba tulu on", maksuvaba_tulu, "aastas.")
elif aastatulu > 25200:
    print("maksuvaba tulu on 0 eurot")