aastatulu = int(input('Sisesta aastatulu: '))

if aastatulu <= 6000:
    print('maksuvaba_tulu on ', aastatulu)
elif aastatulu >= 6000 and aastatulu <= 14400:
    print('maksuvaba_tulu aastas on 6000 eurot')
       
elif aastatulu >= 14400 and aastatulu <= 25200:
    maksuvaba_tulu = 6000 - 6000 / 10800 * (aastatulu - 14400)
    print('maksuvaba_tulu on: ',maksuvaba_tulu, round(maksuvaba_tulu, 2))

elif aastatulu >= 25200:
    print('maksuvaba_tulu 0 eurot')

