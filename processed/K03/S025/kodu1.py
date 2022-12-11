aastatulu = float(input('Sisestage oma aastatulu: '))

while aastatulu < 0:
    print('Aastatulu ei saa olla negatiivne arv.')
    float(input('Sisestage oma aastatulu: '))
if aastatulu <= 6000:
    print('Teie maksuvaba tulu on', round(aastatulu, 2), 'eurot.')
elif 6000 < aastatulu <= 14400:
    print('Teie maksuvaba tulu on 6000 eurot.')
elif 14400 < aastatulu <= 25200:
    a = 6000 - 6000 / 10800 * (aastatulu - 14400)
    print('Teie maksuvaba tulu on', round(a, 2), 'eurot.')
else:
    print('Teie maksuvaba tulu on 0 eurot.')