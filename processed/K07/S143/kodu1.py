def poisse_ja_tüdrukuid(s):
    return (lambda x: tuple([x.count("P"),x.count("T")]))([y.split()[-1] for y in s])

#print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))