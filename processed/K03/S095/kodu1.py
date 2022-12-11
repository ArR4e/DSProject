aastatulu=float()
while aastatulu <=0:
    aastatulu=float(input("Sisesta aastatulu: "))
if aastatulu<=6000:
    print("Maksuvaba tulu on", round(aastatulu, 2), "eurot")
elif aastatulu<=14400:
    print("Maksuvaba tulu on 6000.0 eurot")
elif 14400<aastatulu<=25200:
    aastatulu=6000-6000/10800*(aastatulu-14400)
    print("Maksuvaba tulu on", round(aastatulu, 2), "eurot")
elif aastatulu>25200:
    print("Maksuvabatulu on 0 eurot")