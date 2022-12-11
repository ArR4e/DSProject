x = float(input('Sisestage aastatulu: '))
y = 'Teie maksuvaba tulu on:'

if x < 6000:
    print(y, str(float(round(x, 2))))
elif x >= 6000 and x < 14400:
    print(y, str(6000))
elif x >= 14400 and x < 25200:
    print(y, str(float(round(6000 - 6000 / 10800 * (x - 14400), 2))))
else:
    print(y, str(0))