tulu = float(input("Sisesta aastatulu: "))
if tulu <= 6000:
    print("Maksuvaba tulu on " + str(round(tulu, 2))+ " eurot")
elif 6000 <= tulu <= 14400:
    print("Maksuvaba tulu on 6000 eurot")
elif 14400 <= tulu <= 25200:
    print("Maksuvaba tulu on " + str(round(6000 - 6000 / 10800 * (tulu - 14400),2)))
elif 25200 <= tulu:
    print("Maksuvaba tulu on 0 eurot")