aastatulu = float(input("Kirjuta siia oma aastatulu: "))

if aastatulu > 25200:
    print("Teie maksuvaba tulu on 0 eurot.")
elif aastatulu > 14400:
    tulu3 = float(6000-6000/10800*(aastatulu-14400))
    tulu3 = round(tulu3, 2)
    print("Teie maksuvaba tulu on " + str(tulu3) + " eurot.")
elif aastatulu > 6000:
    print("Teie maksuvaba tulu on 6000 eurot aastas")
else:
    print("Teie maksuvaba tulu on võrdne teie aastatuluga.")
    