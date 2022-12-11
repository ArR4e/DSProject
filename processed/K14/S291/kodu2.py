def väljasta_liin(eellase_nimi, järglase_nimi, sugupuu_sõnastik):
    for võti in sugupuu_sõnastik:
        if sugupuu_sõnastik[võti][0] == eellase_nimi or sugupuu_sõnastik[võti][1] == eellase_nimi:
            print(eellase_nimi)
            if võti == järglase_nimi:
                print(järglase_nimi)
                break
            else:
                väljasta_liin(võti, järglase_nimi, sugupuu_sõnastik)
    return True

# sõnastik = {
#   'Kalle': ('Teet', 'Maris'),
#   'Maris': ('Konstantin', 'Mari'),
#   'Rita': ('Teet', 'Maris'),
#   'Siim': ('Teet', 'Maris'),
#   'Mari': ('Karl', 'Leeni'),
#   'Teet': ('Joosep', 'Adele'),
#   'Adele': ('Johannes', 'Leida'),
#   'Konstantin': ('Viktor', 'Jelena'),
#   'Joosep': ('August', 'Emma'),
#   'Viktor': ('Nikolai', 'Maria')}
# 
# print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sõnastik))