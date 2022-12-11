
aastatulu = float(input("Sisestage aastatulu: "))

if (aastatulu < 6000.0):
    print(round(aastatulu, 2))

elif(6000.0 <= aastatulu < 14400.0):
    print(6000.00)

elif(14400.00 <= aastatulu < 25200.00):
    print(round((6000 - 6000 / 10800 * (aastatulu - 14400)), 2))

elif(aastatulu >= 25200):
    print(0.00)

