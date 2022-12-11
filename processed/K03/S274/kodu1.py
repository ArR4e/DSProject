tulu = float(input("Sisesta aastatulu: "))

if tulu < 6000 and tulu >= 0:
    tulu = round(tulu, 2)
    print("Maksuvaba tulu on", tulu, "eurot.")
elif tulu >= 6000 and tulu < 14400:
    tulu = round(tulu, 2)
    print("Maksuvaba tulu on 6000.00 eurot.")
elif tulu >= 14400 and tulu <= 25200:
    mvtulu = 6000 - 6000 / 10800 * (tulu - 14400)
    mvtulu = round(mvtulu, 2)
    print("Maksuvaba tulu on", mvtulu, "eurot.")
else:
    if tulu < 0:
        print("Sisesta mittenegatiivne ujukomaarv :)")
    else:
        tulu = round(tulu, 2)
        print("Maksuvaba tulu on 0.00 eurot.")        
            