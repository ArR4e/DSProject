hind = float(input('Sisestage auto hind: '))
aastad = int(input('Sisestage auto vanus aastates: '))

def auto_hind(hind, aastad):
    if hind == 0:
        return 0
    elif aastad == 0:
        return hind
    elif aastad >= 0:
        return auto_hind(round(0.8*hind, 2), aastad-1)


väärtus = auto_hind(hind, aastad)
print('Auto väärtus on ', väärtus)