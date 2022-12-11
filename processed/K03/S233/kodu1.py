aastatulu = float(input("Sisestage aastatulu: "))

if aastatulu <= 6000:
    print(aastatulu)
elif aastatulu > 6000 and aastatulu <= 14400:
    print("Maksuvaba tulu on "+" 6000 eurot")
elif aastatulu > 14400 and aastatulu <= 25200:
    print("Maksuvaba tulu on", round(6000-6000/10800*(aastatulu-14400),2))
else:
    print("Maksuvaba tulu on 0 eurot")