tulu = float(input("Sisesta aastatulu: "))
while tulu > 0:
    if tulu <= 6000:
        print("Maksuvaba tulu on: " + str(round(tulu, 2)))
    elif 6000 < tulu <= 14400:
        print("Maksuvaba tulu on: 6000")
    elif 14400 < tulu <= 25200:
        print("Maksuvaba tulu on: " + str(round((6000-6000/10800*(tulu-14400)), 2)))
    elif tulu > 25200:
        print("Maksuvaba tulu on: 0")
    break