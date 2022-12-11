tulu = float(input('Sisestage aastatulu: '))

if tulu <= 6000:
    vaba = tulu
elif tulu <= 14400:
    vaba = 6000
elif tulu <= 25200:
    vaba = round(6000 - 6000 / 10800 * (tulu - 14400), 2)
else:
    vaba = 0
print('Maksuvaba tulu on ', vaba, 'eurot.')