tulu = int(input("Aastatulu: "))
if tulu <= 6000:
    print(tulu)
elif tulu <= 14400:
    print(6000)
elif tulu <= 25200:
    print(round(6000-6000/10800*(tulu-14400),2))
else:
    print(0)