sõnastik= {
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
def väljasta_liin(eellane,järglane,s6nastik):
    for eellane in s6nastik:
        if s6nastik[eellane] == None:
            return 1
        else:
            return väljasta_liin(eellane[i+1], järglane, sõnastik)

print(väljasta_liin('Kalle','Karl',sõnastik))