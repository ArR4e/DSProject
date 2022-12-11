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

def väljasta_liin(eelase_nimi, järglase_nimi, sugupuu):
    if järglase_nimi not in sugupuu:
        return False
    else: 
        if sugupuu[järglase_nimi][0] == eelase_nimi or sugupuu[järglase_nimi][1] == eelase_nimi:
            print(eelase_nimi + "\n" + järglase_nimi)
            return True
        elif väljasta_liin(eelase_nimi, sugupuu[järglase_nimi][0], sugupuu) or väljasta_liin(eelase_nimi, sugupuu[järglase_nimi][1], sugupuu):
            print(järglase_nimi)
            return True
    return False
    

print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sõnastik))
#print("Kas liin leidub?", väljasta_liin('Mari', 'Adele', sõnastik))
print("Kas liin leidub?", väljasta_liin('A', 'Adele', sõnastik))