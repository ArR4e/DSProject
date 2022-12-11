x = int(input("Sisesta aastatulu: "))

if x <= 6000:
    print("Maksuvaba tulu on " + str(x))
elif x <= 14400:
    print("Maksuvaba tulu on 6000")
elif x <= 25200:
    y = round(6000-6000/10800*(x - 14400), 2)
    print("Maksuvaba tulu on " + str(y))
else:
    print("Maksuvaba tulu on 0 eurot")