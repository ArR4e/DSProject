tulu = float(input("Sisesta oma aastatulu: "))
if tulu < 6000:
    maksuvaba_tulu = tulu
else:
    if tulu >= 6000 and tulu < 14400:
        maksuvaba_tulu = 6000
    else:
        if tulu >= 14400 and tulu < 25200:
            maksuvaba_tulu = (6000 - 6000 / 10800 * (tulu - 14400))
        else:
            if tulu >= 25200:
                maksuvaba_tulu = 0

print("Maksuvaba tulu on " + str(round(maksuvaba_tulu, 2)) + " eurot.")