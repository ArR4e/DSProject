tulu = float(input("Sisesta aastatulu: "))
Arvutus = round(6000 - 6000/10800 * (tulu - 14400), 2)
if tulu > 25200:
    print("Maksuvaba tulu on 0 eurot.")
else:
    if tulu > 14400:
        print("Maksuvaba tulu on", Arvutus, "eurot.")
    else:
        if tulu > 6000:
            print("Maksuvaba tulu on 6000 eurot.")
        else:
            if tulu <= 6000:
               print("Maksuvaba tulu on", tulu, "eurot.")