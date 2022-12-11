

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


def väljasta_liin(nimi1, nimi2 , sõnastik):
    if nimi2 in sõnastik:
        kiri = sõnastik[nimi2]
        if kiri[0] == nimi1:
            print(kiri[0])
            return True
        if kiri[1] == nimi1:
            print(kiri[1])
            return True
        if väljasta_liin(nimi1, kiri[0] , sõnastik) is True:
            print(kiri[0])
            if kiri[0] != nimi2:
                print(nimi2)
            return True
        if väljasta_liin(nimi1, kiri[1] , sõnastik) is True:
            print(kiri[1])
            if kiri[1] != nimi2:
                print(nimi2)
            return True
        if väljasta_liin(nimi1, kiri[0] , sõnastik) is False or väljasta_liin(nimi1, kiri[1] , sõnastik) is False:
            return False
    if nimi2 not in sõnastik:
        return False
    

väljasta_liin('Leida', 'Kalle', sõnastik)