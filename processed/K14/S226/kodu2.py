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
# key = nimi, value = tuple type, 0 indeks = isa, 1indeks = ema
# 
# x = sõnastik.values()
# print(type(x))
# if "Teet" in x:
#     print(True)
# 
# for key in s:
#     if "Leida" in s[key]:
#         print(key)

#LEIDA is mother of Adele
def väljasta_liin(eellase_nimi, jarglase_nimi, sugupuu):
   for key in sugupuu:
        if eellase_nimi in sugupuu[key]:
            print(key)
            if key == jarglase_nimi:
                break
            väljasta_liin(key, jarglase_nimi, sugupuu)
#когда и как проверять конкретную личность у кого этот челик стал отцом?
#print(väljasta_liin('Leida', 'Kalle', s))
print(väljasta_liin('Mari', 'Adele', s))
            
    
    
    