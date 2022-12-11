tulu = float(input("Sisesta aastane tulu: "))

if tulu > 0:
    if tulu <= 6000:
        print("Aastane tulumaksu tulu on: " + str(tulu) )
    else:
        if tulu <= 14400:
            print("Aastane tulumaksu vaba tulu on: 6000 " )
        else:
            if (tulu > 14400) and (tulu <= 25200) :
                x = round((6000 - (6000 / 10800) * (tulu - 14400)) , 2)
                print("Aastane tulumaksu vaba tulu on: " + str(x) )
else:
    print("Midagi läks valesti")