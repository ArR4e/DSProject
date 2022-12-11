a = float(input("Sisetage palun oma aastatulu: "))
if a <= 6000:
    print(f"Sinu maksuvaba tulu on {round(a, 2)} eurot.")
elif 6000 < a <= 14400:
    print("Sinu maksuvaba tulu on 6000.00 eurot.")
elif 14400 < a <= 25200:
    print(f"Sinu maksuvaba tulu on {round(6000 - 6000 / 10800 * (a - 14400), 2)} eurot.")
else:
    print("Sinu maksuvaba tulu on 0.00 eurot.")