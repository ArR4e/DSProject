t = float(input('Sisestage oma aasta sissetulek: '))
if t <= 6000:
    round(t, 2)
    print('Teie maksuvaba tulu on ', str(t))
elif 6000 < t and t <= 14400:
    print('Teie maksuvaba tulu on 6000')
elif 1440 < t and t <= 25200:
    t = 6000 - 6000 / 10800 * (t - 14400)
    print('Teie maksuvaba tulu on ', str(round(t, 2)))
else: #t<25200
    t = 6000 - 6000 / 10800 * t
    print('Teie maksuvaba tulu on ', str(round(t, 2)))
    
    