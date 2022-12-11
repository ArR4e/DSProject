aastatulu = float(input('Sisesta oma aastatulu: '))

if aastatulu < 0:
    print('Arv peab olema positiivne')
    quit()
elif aastatulu <= 6000:
    maksuvaba = aastatulu
elif 6000 < aastatulu <= 14400:
    maksuvaba = 6000
elif 14400 < aastatulu < 25200:
    maksuvaba = round((6000 - 6000 / 10800 * (aastatulu - 14400)), 2)
else:
    maksuvaba = 0

print('Maksuvaba tulu on', maksuvaba)
