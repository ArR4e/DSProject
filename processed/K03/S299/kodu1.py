aastatulu= float(input('Sisestage oma aastatulu: '))

arvutus = (6000 - 6000/10800*(aastatulu - 14400))

if aastatulu < 6000:
    print('Maksuvaba tulu on', aastatulu)
else:
    if aastatulu > 6000 and aastatulu < 14400:
        print('Maksuvaba tulu on 6000')
    else:
        if aastatulu > 14400 and aastatulu < 25200:
             print('Maksuvaba tulu on', round(arvutus,2))
        else:
            if aastatulu > 25200:
                print('Maksuvaba tulu on 0')