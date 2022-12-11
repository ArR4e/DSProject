at = float(input("Palun sisetage oma aastatulu: "))

if at <= 6000:
    mvt = at
elif at > 6000 and at < 14400:
    mvt = 6000
elif at >= 14400 and at < 25200:
    mvt = 6000 - 6000 / 10800 * (at - 14400)
else:
    mvt = 0

print("Teie maksuvaba tulu on: " + str(round(mvt, 2)))