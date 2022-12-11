tulu=float(input("Palun sisesta enda aastatulu: "))

if tulu<6000:
    print("Teie maksuvaba tulu on ", tulu, " €")
elif 6000<=tulu<14400:
    print("Teie maksuvaba tulu on ", str(6000.00), " €")
elif 14400<=tulu<25200:
    vaba_tulu=6000-6000/10800*(tulu-14400)
    print("Teie maksuvaba tulu on ", round(vaba_tulu, 2), " €")
else:
    print("Teie maksuvaba tulu on 0.00 €")