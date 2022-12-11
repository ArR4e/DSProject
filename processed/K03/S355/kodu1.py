aastatulu = float(input("Sisesta oma aastatulu: "))
rikkaAastaTulu = (6000 - (6000/10800 * (aastatulu - 14400)))
rikkaAastaTulu = round(rikkaAastaTulu, 2)
if aastatulu < 0:
    print("aastatulu ei saa olla negatiivne! Proovi uuesti")
else:
    if aastatulu <= 6000:
        print("Maksuvaba tulu on", aastatulu, "eurot!")
    elif aastatulu > 6000:
        if aastatulu <= 14400:
            print("Maksuvaba tulu on 6000 eurot")
        elif aastatulu > 14400:
            if aastatulu < 25200:
                print ("Maksuvaba tulu on", rikkaAastaTulu, "eurot")
            else:
                print("Maksuvaba tulu on 0 eurot")
        
