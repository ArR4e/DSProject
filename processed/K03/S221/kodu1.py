tulu = float(input('Sisesta aastatulu '))

if tulu <= 6000:
    print('Maksuvaba tulu on ', round(tulu, 2), ' eurot.')
elif 6000 < tulu <= 14400:
    print('Maksuvaba tulu on 6000.00 eurot')
elif 14400 < tulu <=25200:
    print('Maksuvabatulu on ', round(6000 - 6000 / 10800 * (tulu - 14400), 2), ' eurot.'  )
elif tulu > 25200:
    print('Maksuvaba tulu on 0.00 eurot')