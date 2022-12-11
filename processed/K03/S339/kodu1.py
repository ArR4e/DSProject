a = float(input("Sisesta aastatulu: "))
b = 6000 - 6000/10800*(a - 14400)
if a < 6000:
    print("Maksuvaba tulu on", round(a), "eurot")
elif 6000 <= a < 14400:
    print("Maksuvaba tulu on 6000 eurot")
elif a >= 25200:
    print("Maksuvaba tulu on 0 eurot.")
elif 14400 <= a < 25200:
    print("Maksuvaba tulu on", round(b, 2), "eurot")