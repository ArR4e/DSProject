def väljasta_liin(eelnimi, järgnimi, sugupuu):
    
    if järgnimi in sugupuu:
        vanemad = sugupuu[järgnimi]
        väljasta_liin(eelnimi, vanemad[0], sugupuu)
        eelnimi = vanemad[1]
    else:
        return False
    print(järgnimi)
    return True

    

sugupuu = {'Kalle': ('Teet', 'Maris'),
          'Maris': ('Konstantin', 'Mari'),
          'Rita': ('Teet', 'Maris'),
          'Siim': ('Teet', 'Maris'),
          'Mari': ('Karl', 'Leeni'),
          'Teet': ('Joosep', 'Adele'),
          'Adele': ('Johannes', 'Leida'),
          'Konstantin': ('Viktor', 'Jelena'),
          'Joosep': ('August', 'Emma'),
          'Viktor': ('Nikolai', 'Maria') }

eelnimi = 'Leida'
järgnimi = 'Kalle'

print("Kas leidub liin?", väljasta_liin(eelnimi,järgnimi,sugupuu))