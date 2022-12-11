def väljasta_liin(eellane, järglane, sõnastik):
    tõene = True
    if eellane == järglane:
        print(eellane)
        return True
    if järglane in sõnastik:
        for vanem in sõnastik[järglane]:
            if väljasta_liin(eellane, vanem, sõnastik):
                print(järglane)
                return True
    return False
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

print(väljasta_liin("Jelena", "Leeni", sõnastik))