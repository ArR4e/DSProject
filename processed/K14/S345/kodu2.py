def väljasta_liin(eellane, järglane, sõnastik):
    if järglane not in sõnastik:
        return False
    elif eellane == väljasta_liin(eellane, sõnastik[järglane][0], sõnastik):
        print(sõnastik[järglane][0])
    elif eellane == väljasta_liin(eellane, sõnastik[järglane][1], sõnastik):
        print(sõnastik[järglane][1])
    else:
        print(järglane)
        return True
        
s = {'Kalle': ('Teet', 'Maris'),'Maris': ('Konstantin', 'Mari'),'Rita': ('Teet', 'Maris'),'Siim': ('Teet', 'Maris'),'Mari': ('Karl', 'Leeni'),'Teet': ('Joosep', 'Adele'),'Adele': ('Johannes', 'Leida'),'Konstantin': ('Viktor', 'Jelena'),'Joosep': ('August', 'Emma'),'Viktor': ('Nikolai', 'Maria')}
print("Kas liin leidub?", väljasta_liin("Leida", "Kalle", s))