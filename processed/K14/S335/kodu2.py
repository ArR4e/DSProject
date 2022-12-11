def väljasta_liin(eel, järg, sõn):
    a = järg
    for nimi, vanemad in sõn.items():
        if nimi == "Viktor" and eel == järg:
            return False
        elif vanemad[0] == eel or vanemad[1] == eel:
            print(eel)
            if vanemad[0] == eel:
                return väljasta_liin(nimi, vanemad[0], sõn)
            elif vanemad[1] == eel:
                return väljasta_liin(nimi, vanemad[1], sõn)
    print(eel)
    return True



sõnastik = {
  'Kalle': ('Teet', 'Maris'),
  'Maris': ('Konstantin', 'Mari'),
  'Rita': ('Teet', 'Maris'),
  'Siim': ('Teet', 'Maris'),
  'Mari': ('Karl', 'Leeni'),
  'Teet': ('Joosep', 'Adele'),
  'Adele': ('Johannes', 'Leida'),
  'Konstantin': ('Viktor', 'Jelena'),
  'Joosep': ('August', 'Emma'),
  'Viktor': ('Nikolai', 'Maria')
}

#print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sõnastik))