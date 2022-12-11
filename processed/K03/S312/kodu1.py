a = float(input('Sisesta aastatulu: '))
if a > 0:
    if a < 6000:
        vaba = a
        print('Maksuvaba tulu on', round(vaba, 2) ,'eurot')
    elif a >= 600 and a < 14400:
        vaba = 6000
        print('Maksuvaba tulu on', round(vaba, 2) ,'eurot')
    elif a >= 14400 and a < 25200:
        vaba = 6000 - (6000 / 10800 * ( a - 14400))
        print('Maksuvaba tulu on', round(vaba, 2) ,'eurot')
    else:
        vaba = 0
        print('Maksuvaba tulu on', round(vaba, 2) ,'eurot')       
else:
    print('Sisestatud aastatulu peab olema positiivne!')



              