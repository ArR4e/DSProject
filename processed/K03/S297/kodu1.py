aastatulu = float(input('Sisestage oma aastatulu:'))
vastus ='Teie aastane maksuvaba tulu on: '

if aastatulu <= 6000 :
    print(vastus + str(aastatulu) + ' eurot.')
elif 6000 < aastatulu <= 14400 :
    print(vastus + '6000 eurot.')
elif 14400 < aastatulu <= 25200 :
    keeruline_arvutus = round(6000 - 6000 / 10800 * (aastatulu - 14400), 2)
    print(vastus + str(keeruline_arvutus) + ' eurot.')
elif 25200 < aastatulu :
    print(vastus + '0 eurot.')