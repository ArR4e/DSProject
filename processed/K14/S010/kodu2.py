sõnastik={
  'Kalle': ('Teet', 'Maris'), # JÄRGLANE:(ISA, EMA)
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
def väljasta_liin(eellane, järglane, sõnastik):
    if eellane in sõnastik[järglane]:
        print(eellane)
        return True
    else:
        isa, ema=sõnastik[järglane]
        if isa in sõnastik:
            väljasta_liin(eellane, isa, sõnastik)  # Pärast seda, kui tuvastatakse, et Joosepi vanemad ei sobi, ning kuvatakse Leida ja tagastatakse True, läheb programm katki. Ei tea, kuidas seda parandada.
            if ema in sõnastik:
                väljasta_liin(eellane, ema, sõnastik)
            else:
                return False
            
            

print('Kas liin leidub?', väljasta_liin('Leida', 'Kalle', sõnastik))