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

def väljasta_liin(eellane, järglane, sõnastik):
    vanemad = list(sõnastik.values())
    järglased = list(sõnastik.keys())
    võimalik_eellane = []
    if eellane in võimalik_eellane:
        return võimalik_eellane
    else:
        for i in range(2):
            võimalik_eellane.append(sõnastik[järglane][i])
            uus_eellane = võimalik_eellane
            järglane = eellane
            eellane = uus_eellane
            väljasta_liin(eellane, järglane, sõnastik)
        print()

print(väljasta_liin('Leida', 'Kalle', sõnastik))