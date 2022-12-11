a = 0
c = 0
d = 0
järjend = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']
def poisse_ja_tüdrukuid(x):
    for rida in järjend:
        a = 0
        nimi1 = järjend[a]
        nimi1 = nimi1[-1]
        a += 1
        if nimi1 == 'P':
            c += 1
        elif nimi1 == 'T':
            d += 1
        else:
            print('vale formaat')
    järjend2 = [c,d]
    return järjend2
poisse_ja_tüdrukuid(järjend)
print(järjend2)