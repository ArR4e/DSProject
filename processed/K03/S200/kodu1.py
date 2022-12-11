aastatulu = float(input("Palun sisestage aastatulu: "))

if aastatulu > 0 and aastatulu < 6000:
    print("Maksuvaba tulu:", round(aastatulu,2))
elif aastatulu >= 6000 and aastatulu < 14400:
    print("Maksuvaba tulu: 6000")
elif aastatulu >= 14400 and aastatulu < 25200:
    maksuvaba = 6000 - 6000 / 10800 * (aastatulu - 14400)
    print("Maksuvaba tulu:", round(maksuvaba,2))
elif aastatulu >= 25200:
    print("Maksuvaba tulu: 0")
else:
    print("Palun sisestada mittenegatiivne arv")

