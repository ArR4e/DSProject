#Väljasta liin
# Funktsioon põhimõtteliselt töötab, kuid ma ei suutnud panna seda viimast nime väljastama

def väljasta_liin(eellane, järglane, sugupuu):
    if järglane in sugupuu:
        if eellane in sugupuu[järglane]:
            print(eellane)
            return True
        elif väljasta_liin(eellane, sugupuu[järglane][0], sugupuu):  #Vaatab kas isapoolses sugupuus leidub eellane
            print(sugupuu[järglane][0])
            return True
        elif väljasta_liin(eellane, sugupuu[järglane][1], sugupuu):  #Vaatab kas emapoolses sugupuus leidub eellane
            print(sugupuu[järglane][1])
            return True
        else:
            return False
    else:
        return False


sugupuu_sõnastik = {
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
print(f"Kas liin leidub? {väljasta_liin('Leida', 'Kalle', sugupuu_sõnastik)}")