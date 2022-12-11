a = float(input("Sisesta aastatulu: "))

if a < 6000:
    print("Maksuvaba tulu on ", a)
elif 6000 <= int(a) <= 14400:
    print("Maksuvaba tulu on ", 6000)
elif 14401 <= int(a) <= 25200:
     print("Maksuvaba tulu on ", round((6000 - 6000/10800 * (a - 14400)), 2))
elif int(a) >= 25201:
    print("Maksuvaba tulu on ", 0)