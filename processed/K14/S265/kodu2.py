sonastik = {
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

def väljasta_liin(eel, jarg, tree):
    if jarg in tree:
        for i in tree[jarg]:
            if i == eel:
                print(i)
                print(jarg)
                return True
            elif i in tree:
                if väljasta_liin(eel, i, tree) == True:
                    print(jarg)
                    return True
            else:
                pass
    return False

print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sonastik))