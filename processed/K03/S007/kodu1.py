b = ("Maksuvaba tulu on:")
a = float(input("Sisetage aastatulu eurodes: "))

if a < 6000:
        print(b, a)
elif 6000 <= a < 14400:
    print(b + "6000")
elif 14400 <= a < 25200:
    print(b,round (6000 - 6000 / 10800 * (a - 14400),2))
else:
    print(b,0)