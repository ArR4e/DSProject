eesnimi = input("Sisestage oma eesnimi: ")
perenimi = input("Sisestage oma perenimi: ")

väljund = eesnimi.lower() + '.' + perenimi.lower()
keymap = {'ä': 'a', 'ö': 'o', 'õ': 'o', 'ü': 'u'}

for täht in väljund:
    if täht in keymap:
        väljund = väljund.replace(täht, keymap[täht])
        
print(väljund)