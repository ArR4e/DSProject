aastatulu = float(input('Sisestage aastatulu: '))
if aastatulu <= 6000:
    print('Maksuvaba tulu on ' + str(round(aastatulu, 2)) + ' eurot.')
elif aastatulu > 6000 and aastatulu <= 14400:
    print('Maksuvaba tulu on 6000 eurot.')
elif aastatulu > 14400 and aastatulu <= 25200:
    aastatulu = 6000 -6000 / 10800 * (aastatulu - 14400)
    print('Maksuvaba tulu on ' + str(round(aastatulu, 2)) + ' eurot.')
else:
    print('Maksuvaba tulu on 0 eurot')