aastatulu = float(input("Sisesta aastatulu: "))
maksuvaba_tulu_arvutus = round(6000 - 6000/10800*(aastatulu - 14400),2)
if aastatulu <=6000:
    print("Maksuvaba tulu on " + str(aastatulu) + " eurot.")
else:
    if aastatulu > 6000 and aastatulu <= 14400:
        print("Maksuvaba tulu on 6000 eurot.")
    else:
        if aastatulu > 14400 and aastatulu <= 25200:
            print("Maksuvaba tulu on " + str(maksuvaba_tulu_arvutus) + " eurot.")
        else:
            if aastatulu > 25200:
                print("Maksuvaba tulu on 0 eurot")
                    