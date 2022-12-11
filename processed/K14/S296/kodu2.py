# sõnastik = {
#   'Kalle': ('Teet', 'Maris'),
#   'Maris': ('Konstantin', 'Mari'),
#   'Rita': ('Teet', 'Maris'),
#    'Siim': ('Teet', 'Maris'),
#   'Mari': ('Karl', 'Leeni'),
#    'Teet': ('Joosep', 'Adele'),
#   'Adele': ('Johannes', 'Leida'),
#    'Konstantin': ('Viktor', 'Jelena'),
#    'Joosep': ('August', 'Emma'),
#    'Viktor': ('Nikolai', 'Maria')
# }
def väljasta_liin(eellane, järglane, sõnastik):
    if järglane == eellane:
        print(eellane)
        return True
    if järglane in sõnastik:
        for i in sõnastik:
            if i == järglane:
                for j in sõnastik[i]:
                    a=väljasta_liin(eellane,j,sõnastik)
                    if a == True:
                        print(järglane)
                        return True
                return a
    elif järglane not in sõnastik:
        a=False
        return a

                    

#print("Kas liin leidub?", väljasta_liin('Mari', 'Adele', sõnastik))
