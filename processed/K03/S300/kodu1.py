tulu_arv = input("Sisesta aastatulu: ")
aastatulu = float(tulu_arv)

if aastatulu <= 6000:
    print(aastatulu)
else:
    if aastatulu > 6000 and aastatulu <= 14400:
        print(6000)
    else:
        if aastatulu > 14400 and aastatulu <= 25200:
            print(round(6000 - 6000 / 10800 * (aastatulu - 14400), 2))
        else:
            print(0)
    
    