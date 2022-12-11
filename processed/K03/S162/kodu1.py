aastatulu=float(input("sisesta aastatulu eurodes: "))
if aastatulu<0:
    print("tulu polegi, ainult kulud")
else:
    if aastatulu<6000:
        maksuvaba=aastatulu
    if aastatulu>=6000 and aastatulu<14400:
        maksuvaba=6000
    if aastatulu>=14400 and aastatulu<=25200:
        maksuvaba=6000-6000/10800*(aastatulu-14400)
    if aastatulu>25200:
        maksuvaba=0
    print(round(maksuvaba,2))