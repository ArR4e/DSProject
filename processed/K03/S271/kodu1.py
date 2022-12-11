aasta_tulu = float(input('Aasta tulu?'))

if aasta_tulu < 6000:
    maksuta = round(aasta_tulu, 2)
elif aasta_tulu >= 6000 and aasta_tulu < 14400:
    maksuta = 6000
elif aasta_tulu >= 14400 and aasta_tulu <= 25200:
    maksuta = round(6000 - 6000 / 10800 * (aasta_tulu - 14400), 2)
else:
    maksuta = 0

print(maksuta)
