tulu=float(input("Sisesta aastatulu: "))
if tulu>0:
    if tulu<=6000:
        print("Maksuvaba tulu on",round(tulu,2),"€")
    elif tulu>6000 and tulu<=14400:
        vaba=round((tulu-6000),2)
        print("Maksuvaba tulu on 6000 €")
    elif tulu>14400 and tulu<=25200:
        vaba=round((6000-(6000/10800)*(tulu-14400)),2)
        print("Maksuvaba tulu on",vaba,"€")
    else:
        print("Maksuvaba tulu on 0.00€")
else:
    print("Midagi läks valesti")