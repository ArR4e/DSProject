# alustasin 11.09.2021 (23:17)
aastatulu = float(input('Sisesta aastatulu: '))
if aastatulu < 0:
    print('Aastatulu ei saa olla negatiivne')
    quit()
else:
    if aastatulu <= 6000:
        maksuvabatulu = aastatulu
    elif 6000 < aastatulu <= 14400:
        maksuvabatulu = 6000
    elif 14400 < aastatulu <= 25200:
        maksuvabatulu = 6000-6000/10800*(aastatulu - 14400)
    else:
        maksuvabatulu = 0
        
print('Maksuvaba tulu on ' + str(round(maksuvabatulu, 2)) + ' eurot.')