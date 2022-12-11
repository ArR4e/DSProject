tulu=float(input('Sisesta aastatulu: '))

round(tulu,2)

if tulu>25200:
    vaba=0
elif 14400<tulu<=25200:
    vaba=6000-(6000/10800*(tulu-14400))
elif 6000<tulu<=14400:
    vaba=6000
else:
    vaba=tulu

print('Maksuvaba tulu on', str(round(vaba,2)), 'eurot')