a = float(input("Sisestage aastatulu: "))

if a <= 6000:
    print("Maksuvaba tulu on " + str(a) + " eurot.")
elif a > 6000 and a < 14401:
    print("Maksuvaba tulu on 6000 eurot.")
elif a > 14400 and a < 25201:
    a = 6000 - 6000/10800*(a-14400)
    print("Maksuvaba tulu on " + str(round(a,2)) + " eurot.")
else:
    print("Maksuvaba tulu on 0 eurot.")