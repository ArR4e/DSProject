aastatulu = float(input('Sisesta aastatulu: '))

if aastatulu <= 6000:
    maksuvaba = aastatulu
    
elif 6000 < aastatulu <= 14400:
    maksuvaba = 6000
    
elif 14400 < aastatulu <= 25200:
    maksuvaba = 6000 -6000 / 10800 * (aastatulu - 14400)
    
elif aastatulu > 25200:
    maksuvaba = 0


a = round(maksuvaba, 2)
print('Maksuvaba tulu on '+ str(a) +' eurot.')