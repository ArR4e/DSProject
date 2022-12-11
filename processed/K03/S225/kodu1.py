a = int(input('Sisestage aastatulu: '))

if a <= 6000:
    print('Maksuvaba tulu on', a, 'eurot.')
    
else:
    if 6000 < a <= 14400:
        b = round(6000 - 6000 / 10800 * (a - 14400), 2)
        print('Maksuvaba tulu on', b, 'eurot.')
    
    else:
        c = round(6000 - 6000 / 10800 * (a - 14400), 2)
        print('Maksuvaba tulu on', c, 'eurot.')
