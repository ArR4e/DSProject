sisend = input('Sisestage oma aastatulu: ')
tulu = float(sisend)

if tulu <= 6000:
        print('Maksuvaba tulu on', tulu, 'eurot.')
elif tulu > 6000 and tulu <= 14400:
    print('Maksuvaba tulu on', '6000', 'eurot.')
elif tulu > 14400 and tulu <= 25200:
    vaba = round(float(6000 - 6000/ 10800*(tulu - 14400)), 2)
    print(vaba)
elif tulu > 25200:
    print('Maksuvaba tulu on', '0', 'eurot.')



