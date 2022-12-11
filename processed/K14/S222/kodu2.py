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

def väljasta_liin(e,j,s):
    if e in s[j]:
        return True
    else:
        for järglane in s:
            if e in s[järglane]:
                return väljasta_liin(järglane,j,s)
    return False
print(väljasta_liin("Leida","Kalle",s))
print(väljasta_liin("Mari","Adele",s))
            