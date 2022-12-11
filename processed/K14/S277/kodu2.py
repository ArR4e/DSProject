sõnastik ={
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

def väljasta_liin(eellane, jarglane, sõnastik):
    for jarglase_vanem in sõnastik[jarglane]:
        if eellane != jarglase_vanem:
            try:
                if valjasta_liin(eellane, jarglase_vanem, sõnastik) is True: #Kas see ei ole rekursioon?
                    print(jarglane)
                    return True
            except:
                pass
        elif eellane == jarglase_vanem:
            print(eellane)
            print(jarglane)
            return True
    return False
        
print('Kas liin leidub?', väljasta_liin('Mari', 'Adele', sõnastik))


