# 2. Väljasta liin
# Kirjuta rekursiivne funktsioon väljasta_liin, mis võtab argumentideks eellase nime, järglase nime ja
# sugupuu sõnastiku ning väljastab ekraanile põlvnemiste ahela eellasest järglaseni, kui selline ahel leidub.
# Kui ahelat ei leidu, siis ei tohiks funktsioon midagi välja printida.
# Lisaks peab funktsioon tagastama tõeväärtuse True või False vastavalt sellele, kas liin leidub või ei.
# Sõnastikus on võtmeks sõnena nimi ning väärtuseks ennikuna (või järjendina) isa nimi indeksil 0 ja ema nimi indeksil 1.

# Näide programmi tööst (sõnastiku väljund on ilustatud):

#sõnastik = {'Kalle': ('Teet', 'Maris'),
#            'Maris': ('Konstantin', 'Mari'),
#            'Rita': ('Teet', 'Maris'),
#            'Siim': ('Teet', 'Maris'),
#            'Mari': ('Karl', 'Leeni'),
#            'Teet': ('Joosep', 'Adele'),
#            'Adele': ('Johannes', 'Leida'),
#            'Konstantin': ('Viktor', 'Jelena'),
#            'Joosep': ('August', 'Emma'),
#            'Viktor': ('Nikolai', 'Maria')
#            }
 
# >>> print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sõnastik))
#Leida
#Adele
#Teet
#Kalle
#Kas liin leidub? True
 
#>>> print("Kas liin leidub?", väljasta_liin('Mari', 'Adele', sõnastik))
#Kas liin leidub? False

def väljasta_liin(eel, järel, sugupuu):
    if järel not in sugupuu.keys():
        return False
    else:
        print(eel)
        for i in range(len(list(sugupuu))):
            s = list(sugupuu.items())[i]
            nimed = s[1]
            if eel in nimed:
                eel2 = list(sugupuu.keys())[i]
                if eel2 == järel:
                    print(järel)
                    return 
                else:
                    väljasta_liin(eel2, järel, sugupuu)
        return True 
    


