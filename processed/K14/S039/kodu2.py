def väljasta_liin(eellane,järglane,sõnastik):
    if sõnastik[järglane][0]==eellane or sõnastik[järglane][1]==eellane:
        print(eellane)
        return True
    elif sõnastik[järglane][0] not in sõnastik and sõnastik[järglane][1] not in sõnastik:
        return False
    else:
        if väljasta_liin(eellane,sõnastik[järglane][0],sõnastik)==True:
            print(sõnastik[järglane][0])
            return True
        elif väljasta_liin(eellane,sõnastik[järglane][1],sõnastik)==True:
            print(sõnastik[järglane][1])
            return True
        else:
            return False
        
sõnastik={ 'Kalle': ('Teet', 'Maris'),'Maris': ('Konstantin', 'Mari'),'Rita': ('Teet', 'Maris'),'Siim': ('Teet', 'Maris'),'Mari': ('Karl', 'Leeni'),'Teet': ('Joosep', 'Adele'),'Adele': ('Johannes', 'Leida'),'Konstantin': ('Viktor', 'Jelena'),'Joosep': ('August', 'Emma'),'Viktor': ('Nikolai', 'Maria') }
print("Kas liin leidub?",väljasta_liin('Leida', 'Kalle', sõnastik))