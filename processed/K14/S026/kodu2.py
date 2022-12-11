def väljasta_liin(e_nimi, j_nimi, sõnastik):
    järglane = list(sõnastik.keys())
    eellane = list(sõnastik.values())
    for järglane in sõnastik:
        eellased = sõnastik[järglane]
        for eellane in eellased:
            if eellane == e_nimi:
                print(eellane)
                väljasta_liin(järglane, j_nimi, sõnastik)
            else:
                if eellane == j_nimi:
                    print(eellane)
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

väljasta_liin("Maris", "Karl", sõnastik)