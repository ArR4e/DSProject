sõnastik = {
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
#A on B eellane, kui ta on B ema/isa või kui ta on B ema/isa eellane.
def väljasta_liin(eellane, järglane, sõnastik):
    if järglane in sõnastik.keys():
        väljasta_liin(sõnastik, sõnastik[järglane][0], sõnastik)
        väljasta_liin(sõnastik, sõnastik[järglane][1], sõnastik)
    else:
        return 0
väljasta_liin('Leida', 'Kalle', sõnastik)