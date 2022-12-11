at = float(input("Sisesta aastatulu: "))
if at <= 6000:
    print("Maksuvaba tulu on " + str(at) + " eurot.")
elif at <= 14400:
    print("Maksuvaba tulu on 6000 eurot.")
elif at <= 25200:
    mv = 6000 - (6000 / 10800 * (at - 14400))
    print("Maksuvaba tulu on " + str(round(mv, 2)) + " eurot.")
else:
    print("Maksuvaba tulu on 0 eurot.")
