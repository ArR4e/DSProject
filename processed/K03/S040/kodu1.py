a = int(input("Sisesta aastatulu: "))
b = round(6000 - 6000 / 10800 * (a - 14400), 2)
if a < 6000:
    print("Maksuvaba tulu on " + str(a) + " eurot")
else:
    if a >= 6000 and a < 14400:
        print("Maksuvaba tulu on 6000 eurot")
    else:
        if a >= 14400 and a < 25200:
            print("Maksuvaba tulu on " + str(b) + " eurot")
        else:
            print("Maksuvaba tulu on 0 eurot")