tulu = float(input("Sisesta aastatulu: "))
if tulu < 6000:
    print("Maksuvaba tulu on", round(tulu, 2), "eurot.")

elif tulu >= 6000 and tulu < 14400:
    print("Maksuvaba tulu on 6000 eurot.")
elif tulu >= 14400 and tulu < 25500:
    print("Maksuvaba tulu on", round(6000-6000/10800 * (tulu - 14400), 2), "eurot.")
else:
    print("Maksuvaba tulu on 0 eurot.")
            




