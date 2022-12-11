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

def väljasta_liin(e_nimi, j_nimi, sõnastik):
    for nimi in sõnastik: 
        if nimi == j_nimi:
            isa, ema = sõnastik[nimi] 
            if e_nimi == isa or e_nimi == ema:
                print(e_nimi)
                print(j_nimi)
                return True
            elif väljasta_liin(e_nimi, isa, sõnastik):
                print(j_nimi)
                return True
            elif väljasta_liin(e_nimi, ema, sõnastik):
                print(j_nimi)
                return True
    return False
        

#print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sõnastik))
#print("Kas liin leidub?", väljasta_liin('Mari', 'Adele', sõnastik))