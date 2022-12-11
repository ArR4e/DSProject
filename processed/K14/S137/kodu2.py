andmed = []
def väljasta_liin(eel_nimi,järg_nimi,sugupuu):
    global andmed
    if järg_nimi not in sugupuu:
        return False
    eellased = sugupuu.values()
    for i in eellased: 
        if eel_nimi in i:
            if sugupuu[järg_nimi] == i:
                andmed.append(eel_nimi)
                andmed.append(järg_nimi)
                return True
            else:
                andmed.append(eel_nimi)
                eel_nimi = list(sugupuu.keys())[list(sugupuu.values()).index(i)]
                return väljasta_liin(eel_nimi,järg_nimi,sugupuu)
sonastik = {'Kalle': ('Teet', 'Maris'),'Maris': ('Konstantin', 'Mari'),'Rita': ('Teet', 'Maris'),'Siim': ('Teet', 'Maris'),'Mari': ('Karl', 'Leeni'),'Teet': ('Joosep', 'Adele'),'Adele': ('Johannes', 'Leida'),'Konstantin': ('Viktor', 'Jelena'),'Joosep': ('August', 'Emma'),'Viktor': ('Nikolai', 'Maria')}
ja = väljasta_liin('Leida', 'Kalle',sonastik)
if ja == True:
    for el in andmed:
        print(el)
print('Kas liin leidub',ja)
