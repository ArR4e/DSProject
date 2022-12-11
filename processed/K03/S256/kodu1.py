i = 0
while i == 0:
    tulu = round(float(input("sisesta tulu: ")), 2)
    tulustr = str(tulu)
    maksuvaba = str(round(6000 - (6000 / 10800 * (tulu - 14400)), 2))
    if tulu < 6000:
        print("maksuvaba tulu on " + str(tulu) + " eurot")
    elif 6000 <= tulu < 14400:
        print("maksuvaba tulu on 6000 eurot")
    elif 14400 <= tulu <25200:
        print("maksuvaba tulu on " + str(maksuvaba))
    else:
        print("maksustatud on kogu tulu ehk " + str(tulustr) + " eurot")