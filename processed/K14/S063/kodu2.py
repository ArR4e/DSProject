'''-- Kodutöö nr. 14 - 2. Väljasta liin --'''
####################################################################################################
## Rekursiivne funktsioon võtab argumentideks eellase nime, järglase nime ja sugupuu sõnastiku ning
## väljastab ekraanile ahela eellasest järglaseni, kui selline ahel leidub;
## lisaks tagastab funktsioon tõeväärtuse True või False vastavalt sellele, kas liin leidub või ei. 
def väljasta_liin(eellane, järglane, sugupuu):
    
    # kui eellane võrdub järglasega, siis on leitud ahel
    if eellane == järglane:
        print(järglane)
        return True
    # kui järglast ei leidu sugupuus
    elif järglane not in sugupuu:
        return False
    # rakenda rekursiivselt edasi
    else:
        (isa, ema) = (el for el in sugupuu[järglane])
        if väljasta_liin(eellane, isa, sugupuu) or väljasta_liin(eellane, ema, sugupuu):
            # kui leidub, siis väljasta
            print(järglane)
            return True
        else:
            return False
####################################################################################################
sõnastik = {'Kalle': ('Teet', 'Maris'),
            'Maris': ('Konstantin', 'Mari'),
            'Rita': ('Teet', 'Maris'),
            'Siim': ('Teet', 'Maris'),
            'Mari': ('Karl', 'Leeni'),
            'Teet': ('Joosep', 'Adele'),
            'Adele': ('Johannes', 'Leida'),
            'Konstantin': ('Viktor', 'Jelena'),
            'Joosep': ('August', 'Emma'),
            'Viktor': ('Nikolai', 'Maria')}

print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sõnastik))
print("Kas liin leidub?", väljasta_liin('Mari', 'Adele', sõnastik))
