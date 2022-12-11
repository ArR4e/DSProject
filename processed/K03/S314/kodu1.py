a = float(input("Sisesta aastatulu (€): "))
if a < 0:
    print("Sisesta positiivne arv.")
elif 0 < a <= 6000:
    print("Maksuvaba tulu on: ", a, "eurot")
elif 6000 < a <= 14400:
    print("Maksuvaba tulu on: 6000 eurot")
elif 14400 < a <= 25200:
    print("Maksuvaba tulu on: ", round(6000 - 6000 / 10800 * (a - 14400),2), "eurot")
else:
    print("Maksuvaba tulu on: 0 eurot")