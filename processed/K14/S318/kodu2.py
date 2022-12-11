sõnastik={
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
list1=[]
list2=[]
def väljasta_liin(eellane,järglane,sõnastik):
    global list1,list2
    if len(list2) != 2:
        list2.append(järglane)
        list2.append(eellane)
    for laps in sõnastik:
        for vanem in sõnastik[laps]:
            if vanem == eellane:
                list1.append(vanem)
                return väljasta_liin(laps,vanem,sõnastik)
            elif vanem == järglane:
                list1.append(laps)
        if järglane in list1 and eellane in list1:
            break
    if list2[0] in list1:
        if list2[1] in list1:
            for e in list1:
                print(e)
        return True
    else:
        return False