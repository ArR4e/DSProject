# Kirjuta rekursiivne funktsioon väljasta_liin, mis võtab argumentideks eellase nime, järglase nime ja sugupuu
# sõnastiku ning väljastab ekraanile põlvnemiste ahela eellasest järglaseni, kui selline ahel leidub. Kui ahelat
# ei leidu, siis ei tohiks funktsioon midagi välja printida. Lisaks peab funktsioon tagastama tõeväärtuse True või
# False vastavalt sellele, kas liin leidub või ei. Sõnastikus on võtmeks sõnena nimi ning väärtuseks ennikuna (või
# järjendina) isa nimi indeksil 0 ja ema nimi indeksil 1.

def väljasta_liin(eellane, järglane, sõnastik):
    if eellane == järglane:
        print(eellane)
        return True
    if järglane in sõnastik:
        isa, ema = sõnastik[järglane]
        tõev = väljasta_liin(eellane, isa, sõnastik) or väljasta_liin(eellane, ema, sõnastik)
        if tõev:
            print(järglane)
        return tõev
    else:
        return False
    
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

print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sõnastik))