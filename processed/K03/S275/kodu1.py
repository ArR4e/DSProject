aastatulu = float(input("Sisesta aastatulu: "))
if aastatulu <= 14400 and aastatulu > 6000:
    print("6000")
elif aastatulu <= 6000:
    print(aastatulu)
elif aastatulu >= 25200:
    print("0")
else:
    valem = round(6000 - 6000/10800 * (aastatulu - 14400), 2)
    print("Maksuvaba tulu on " + str(valem)+ " eurot. ")