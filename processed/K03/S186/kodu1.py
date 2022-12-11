aastatulu=float(input("Sisesta aastatulu: "))
if aastatulu<6000:
    print("Maksuvaba tulu on ",aastatulu," eurot.")
else:
    if 6000<aastatulu<14400:
        print("Maksuvaba tulu on 6000 eurot.")
    else:
        if 14400<aastatulu<25200:
            print("Maksuvaba tulu on ",round(6000-6000/10800*(aastatulu-14400), 2))
        else:
            print("Maksuvaba tulu on 0 eurot.")