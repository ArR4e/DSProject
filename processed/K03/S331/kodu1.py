aastatulu = float(input("Sisesta oma aastatulu: "))
if aastatulu <= 6000:
    maksuvabatulu = round(aastatulu, 2)
    print("Sinu maksuvabatulu on ", maksuvabatulu, "€ aastas")
else:
    if aastatulu >= 6000 and aastatulu <= 14400:
        maksuvabatulu = 6000
        print("Sinu maksuvabatulu on ", maksuvabatulu, "€ aastas")
    else:
        if aastatulu >= 14400 and aastatulu <= 25200:
            maksuvabatulu = round(6000-6000/10800*(aastatulu-14400), 2)
            print("Sinu maksuvabatulu on ", maksuvabatulu, "€ aastas")
        else:
            maksuvabatulu = 0
            print("Sinu maksuvabatulu on ", maksuvabatulu, "€ aastas")
