a = float(input("Sisesta aastatulu: "))

if a <= 6000:
    b = a
elif 6000 < a <= 14400:
    b = 6000
elif 14400 < a <= 25200:
    b = 6000 - 6000 / 10800 * (a - 14400)
else:
    b = 0
    

print("Maksuvaba tulu on: ", str(round(b, 2)))