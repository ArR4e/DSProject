tulu=float(input('Palun sisesta oma aastane tulu: '))
if tulu<=6000:
    tulu=round(tulu,2)
    print('Teie maksuvaba tulu on '+str(tulu)+' eurot.')
elif tulu<=14400:
    print('Teie maksuvaba tulu on 6000 eurot.')
elif tulu<=25200:
    tulu=round(6000-6000/10800*(tulu-14400),2)
    print('Teie maksuvaba tulu on '+str(tulu)+' eurot.')
else:
    print('Teie maksuvaba tulu on 0 eurot.')