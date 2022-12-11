aasta_tulu = abs(float(input("Siseta aastatulu: ")))
if aasta_tulu <= 6000:
    print(aasta_tulu)
elif aasta_tulu > 6000 and aasta_tulu <= 14400:
    print(6000)
elif aasta_tulu > 14400 and aasta_tulu <= 25200:
    maksuvaba = 6000 - 6000/10800*(aasta_tulu-14400)
    maksuvaba = round(maksuvaba, 2)
    print(maksuvaba)
else:
    print(0)
    