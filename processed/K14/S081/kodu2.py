def väljasta_liin(eellane, järglane, sugupuu):
    if järglane in sugupuu:
        print(järglane)
        if eellane in sugupuu[järglane]:
            print(eellane)
            return True
        else:
            vanemad = sugupuu[järglane]
            return väljasta_liin(eellane, vanemad[0], sugupuu)
            return väljasta_liin(eellane, vanemad[1], sugupuu)
    else:
        return False



#     if järglane in sugupuu:
#         vanemad = sugupuu[järglane]
#         if eellane in vanemad:
#             print(eellane)
#             print(järglane)
#         else:
#             for i in vanemad:
#                 return väljasta_liin(eellane, i, sugupuu)
#     else:
#         return False
        


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

print(väljasta_liin('August', 'Kalle', sõnastik))