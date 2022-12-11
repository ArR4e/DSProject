proovin, mis ma proovin, kahjuks mina seda välja ei mõtle, sest ma ei saa sellest teemast mitte midagi aru

def väljasta_liin(eelane, järglane, sugupuu):
    if järglane not in sugupuu:
        pass
    if järglane in sugupuu:
        if eelane in sugupuu[järglane]:
            print("Liin leidub")
        else:
            isa = sugupuu[järglane][0]
            ema = sugupuu[järglane][1]
            väljasta_liin(eelane, ema, sugupuu)
            väljasta_liin(eelane, isa, sugupuu)
       
                
sugupuu = {
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

            
print(väljasta_liin('Joosep', 'Maris', sugupuu)) 