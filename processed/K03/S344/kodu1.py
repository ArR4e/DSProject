x = float(input("Sisesta aastatulu: "))

if x <= 5999:
    print("Maksuvaba tulu on: ", round(x, 2), "€")
elif x == 6000 or x <= 14399:
    print("Maksuvaba tulu on: ", 6000, "€")
elif x == 14400 or x <= 25199:
    print("Maksuvaba tulu on: ", round((6000-6000/10800*(x-14400)), 2), "€")
elif x >= 25200:
    print("Maksuvaba tulu on: ", 0, "€")
else:
    print("Sisestati nekstiivne aastatulu")
