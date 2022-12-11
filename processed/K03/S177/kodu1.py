a=float(input("Sisestage oma aastatulu: "))
if a<6000:
    print ("Teie maksuvaba tulu on ", round (a, 2), "€.")
else:
    if 6000<a<14400:
        print ("Teie maksuvaba tulu on 6000.00 €")
    else:
        if 14400<a<25200:
            print ("Teie maksuvaba tulu on ", round((6000-6000/10800*(a-14400)), 2), "€")
        else:
            if a>25200:
                print ("Teil ei ole maksuvaba tulu.")