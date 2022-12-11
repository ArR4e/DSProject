a = float(input('Sisesta aastatulu: '))
valem = 6000 - 6000 / 10800 * (a - 14400)
if a <= 6000:
    print(f'Maksuvaba tulu on {a} eurot.')
elif a <= 14400:
    print('Maksuvabva tulu on 6000 eurot')
elif 14400 < a <= 25200:
    print(f'Maksuvaba tulu on {round(valem, 2)} eurot')
else:
    print('Maksuvaba tulu on 0 eurot')