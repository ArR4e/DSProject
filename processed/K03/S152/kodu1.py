tulu = float(input("Sisestage aastatulu: "))
if tulu < 6000:
    print ("Maksuvaba tulu on: ", tulu)
else:
    if tulu >= 6000 and tulu < 14400:
        print("Maksuvaba tulu on: 6000")
    elif tulu >= 14400 and tulu <=25200:
        arv = round(6000-(6000/10800)*(tulu - 14400),2)
        print ("Maksuvaba tulu on " , arv)
    elif tulu >25200:
        print ("Maksuvaba tulu on 0")