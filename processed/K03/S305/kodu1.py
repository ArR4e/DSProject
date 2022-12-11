m = float(input("Sisesta aastatulu: "))
if m < 6000:
    t = m
elif m >= 6000 and m < 14400:
    t = 6000
elif m >= 14400 and m <= 25200:
    t = 6000 - 6000 / 10800 * (m - 14400)
else:
    t = 0
print("Maksuvaba tulu on", str(round(t, 2)), "eurot.")