tulu = float(input("Sisesta oma aastatulu: "))

if tulu <= 6000 and tulu >= 0:
    print("Teie maksuvaba tulu on ", round(tulu,2),"€")
else:
    if tulu > 6000 and tulu <= 14400:
        print("Teie maksuvaba tulu on 6000€")
    else:
        if tulu > 14400 and tulu <= 25200:
            mvtulu = 6000-6000/10800*(tulu-14400)
            print("Teie maksuvaba tulu on ", round(mvtulu,2))
        else:
            if tulu > 25200:
                print("Teie maksuvaba tulu on 0€")
            else:
                print("Sisestatud arv ei sobi")