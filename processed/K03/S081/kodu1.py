atulu = int(input('Sisesta aastatulu: '))

if atulu < 0:
    print('See ei ole arvutatav.')

elif atulu <= 6000:
    print('Maksuvaba tulu on ' + str(atulu) + ' eurot.')
    
elif atulu > 6000 and atulu <= 14400:
    print('Maksuvaba tulu on 6000 eurot')

elif atulu > 14400 and atulu <=25200:
    t = round((6000-6000/10800*(atulu-14400)), 2)
    print('Maksuvaba tulu on ' + str(t) + ' eurot.')

elif atulu > 25200:
    print('Maksuvaba tulu on 0 eurot')