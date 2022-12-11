x = float(input('Sisesta aastatulu:'))
if  x < 6000:
    print('Makasuvaba tulu on', round(x, 2), 'eurot')
if x >= 6000 and x < 14400:
    print('Makasuvaba tulu on 6000 eurot')
if x >= 14400 and x < 25200:
    y = 6000 - 6000 / 10800 * (x - 14400)
    print('Makasuvaba tulu on', round(y, 2), 'eurot')
if x >= 25200:
    print('Makasuvaba tulu on 0 eurot')
