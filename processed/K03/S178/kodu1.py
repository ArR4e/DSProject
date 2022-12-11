a = float(input('Sisesta oma aastatulu: '))
    
if 6000 > a:
    print('Maksuvaba tulu on eurodes:')
    print(round(a, 3))
elif 14400 > a >= 6000:
    print('Maksuvaba tulu on 6000 eurot.')
elif 25200 > a >= 14000:
    print('Maksuvaba tulu on eurodes:')
    print(round(6000 - 6000 / 10800 * (a - 14400)))
elif a >= 25200:
    print('Maksuvaba tulu on 0 eurot.')