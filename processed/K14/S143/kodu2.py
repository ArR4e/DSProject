def väljasta_liin(p,c,d):
    if p == c:
        print(p)
        return True
    if c in d.keys():
        if väljasta_liin(p,d[c][0],d):
            print(c)
            return True
        elif väljasta_liin(p,d[c][1],d):
            print(c)
            return True
        else:
            return False
    else:
        return False
    
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
print(väljasta_liin('Mari', 'Adele',s))