sõnastik={'Kalle': ('Teet', 'Maris'),'Maris': ('Konstantin', 'Mari'),'Rita': ('Teet', 'Maris'),'Siim': ('Teet', 'Maris'),'Mari': ('Karl', 'Leeni'),'Teet': ('Joosep', 'Adele'),'Adele': ('Johannes', 'Leida'),'Konstantin': ('Viktor', 'Jelena'),'Joosep': ('August', 'Emma'),'Viktor': ('Nikolai', 'Maria')}

def väljasta_liin(eellane, järglane, sõnastik):
    if järglane in sõnastik.keys():
        if eellane in sõnastik[järglane]:
            print(eellane)
            print(järglane)
            return True
        else:
            if järglane in sõnastik.keys():
                if True==väljasta_liin(eellane, sõnastik[järglane][0], sõnastik):
                    print(järglane)
                    return True
                elif True==väljasta_liin(eellane, sõnastik[järglane][1], sõnastik):
                    print(järglane)
                    return True
                else:
                    return False
    else:
        return False
#print("Kas liin leidub?", väljasta_liin('Jaak', 'Kalle', sõnastik))
