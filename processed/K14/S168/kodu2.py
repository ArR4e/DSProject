
bool = False

def väljasta_liin(ancestor, successor, d):
    global bool
    if successor in d:
        if ancestor in d[successor]:
            bool = True
            print(ancestor)
            print(successor)
        else:
            väljasta_liin(ancestor, d[successor][0], d)
            if bool != True:
                väljasta_liin(ancestor, d[successor][1], d)
                if bool == True:
                    print(successor)
            else:
                print(successor)
    return bool


d = {
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

print("Kas liin leidub?", väljasta_liin('Siim', 'Kalle', d))