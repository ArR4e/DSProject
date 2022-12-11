def väljasta_liin(eel, järg, s):
    if eel in s[järg]:
        return eel
    elif s[järg][0] in s:
        väljasta_liin(eel, s[järg][0], s)
    else:
        väljasta_liin(eel, s[järg][1], s)

        

s = {
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