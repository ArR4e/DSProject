tulu = float(input('Sisesta aastatulu: '))

while True:
    
    if tulu <= 6000 and tulu > 0:
        maksuvaba = tulu
    elif tulu > 6000 and tulu <= 14400:
        maksuvaba = 6000
    elif tulu > 14400 and tulu <= 25200:
        maksuvaba = 6000 - 6000 / 10800 * (tulu - 14400)
    elif tulu > 25200:
        maksuvaba = 0
    else:
            print('Pead sisestama positiivse arvu!')
            break
    
    print('Maksuvaba tulu on ' + str(round(maksuvaba, 2)) + ' eurot.')
    break

