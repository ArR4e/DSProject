def hmm(eel, järg, puu):
    ee = list(puu.keys())
    for isik in ee:
        if puu[isik][0] == eel or puu[isik][1] == eel:
            print(isik)
            hmm(isik, järg, puu)
        elif puu[isik] == järg or puu[isik][0] == järg:
            break

            

def väljasta_liin(eel, järg, puu):
    if puu[järg][0] != eel and puu[järg][1] != eel:
        for i in puu[järg]:
            if i in puu:
                väljasta_liin(eel, i, puu)
            elif i not in puu:
                return False

    elif puu[järg][0] == eel or puu[järg][1] == eel:
        print(eel)
        hmm(eel, järg, puu)
    

                
                
puu = {
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


väljasta_liin('Leida', "Kalle", puu)