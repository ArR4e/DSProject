#2. Väljasta liin

def väljasta_liin(ellane, järglane, sugupuu):
    if järglane in sugupuu:
        if ellane in sugupuu[järglane]:
            print(ellane)
            return True
        else:
            for vanem in sugupuu[järglane]:
                if väljasta_liin(ellane, vanem, sugupuu) == True:
                    print(vanem)
                    print(järglane)
                    return True
                else:
                    return False
    else:
        return False
        
sõnastik={'Kalle': ('Teet', 'Maris'),
  'Maris': ('Konstantin', 'Mari'),
  'Rita': ('Teet', 'Maris'),
  'Siim': ('Teet', 'Maris'),
  'Mari': ('Karl', 'Leeni'),
  'Teet': ('Joosep', 'Adele'),
  'Adele': ('Johannes', 'Leida'),
  'Konstantin': ('Viktor', 'Jelena'),
  'Joosep': ('August', 'Emma'),
  'Viktor': ('Nikolai', 'Maria')}

print(väljasta_liin("Leida", "Kalle", sõnastik))
#print(sõnastik["Maris"])