def poisse_ja_tüdrukuid(x):
    m=0
    n=0
    for y in x:
        if y[-1] == 'P':
            m += 1
        elif y[-1] == 'T':
            n += 1
        else:
            pass
    return m,n

print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))
print(type(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])))