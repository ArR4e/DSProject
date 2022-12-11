# s_d = {
#   'Kalle': ('Teet', 'Maris'),
#   'Maris': ('Konstantin', 'Mari'),
#   'Rita': ('Teet', 'Maris'),
#   'Siim': ('Teet', 'Maris'),
#   'Mari': ('Karl', 'Leeni'),
#   'Teet': ('Joosep', 'Adele'),
#   'Adele': ('Johannes', 'Leida'),
#   'Konstantin': ('Viktor', 'Jelena'),
#   'Joosep': ('August', 'Emma'),
#   'Viktor': ('Nikolai', 'Maria')
# }

def väljasta_liin(e_nimi, j_nimi, s_d):
    if e_nimi == j_nimi:
        print(e_nimi)
        return True
    if j_nimi in s_d:
        if väljasta_liin(e_nimi, s_d[j_nimi][0], s_d) == True or väljasta_liin(e_nimi, s_d[j_nimi][1], s_d) == True:
            print(j_nimi)
            return True
        else:
            return False
    else:
        return False
        

#print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', s_d))    