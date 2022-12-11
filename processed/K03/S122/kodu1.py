aastatulu = float(input("Aastatulu: "))

if 0 <= aastatulu <= 6000:
    print('Maksuvaba tulu on ' + str(aastatulu))
elif 6000 < aastatulu <= 14400:
    print('Maksuvaba tulu on 6000 eurot aastas.')
elif 14400 < aastatulu <= 25500:
    arvutus = 6000 - 6000 / 10800 * (aastatulu - 14400)
    ymardus = round(arvutus, 2)
    print('Maksuvaba tulu on ' + str(ymardus) + ' eurot.')
elif aastatulu > 25500:
    print('Maksuvaba tulu on 0 eurot.')
else:
    print('Palun sisesta mittenegatiivne arv!')