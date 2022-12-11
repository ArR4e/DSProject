tulu = float(input("Sisesta aastatulu:"))
if tulu < 6000:
    mvtulu = tulu
elif tulu < 14400:
    mvtulu = 6000
elif tulu < 25200:
    mvtulu = 6000 - 6000 / 10800 * (tulu - 14400)
else:
    mvtulu = 0
print(round(mvtulu, 2))