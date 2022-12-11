income = float(input('Sisesta aastatulu: '))
if income < 6000:
    notax = round(income, 2)
elif income >= 6000 and income < 14400:
    notax = 6000
elif income >= 14400 and income < 25200:
    notax = round(6000 - 6000 / 10800 * (income - 14400), 2)
else:
    notax = 0

print('Maksuvaba tulu on', notax, 'eurot.')