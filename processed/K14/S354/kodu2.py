sõnastik = {'Kalle': ('Teet', 'Maris'),'Maris': ('Konstantin', 'Mari'),
  'Rita': ('Teet', 'Maris'),'Siim': ('Teet', 'Maris'),'Mari': ('Karl', 'Leeni'),
  'Teet': ('Joosep', 'Adele'),'Adele': ('Johannes', 'Leida'),
  'Konstantin': ('Viktor', 'Jelena'),'Joosep': ('August', 'Emma'),
  'Viktor': ('Nikolai', 'Maria')
}
def väljasta_liin(e, j, s):
    if e == j:
        print(e)
        return True
    elif j in s:
        isa, ema = s[j]
        tõeväärtus = väljasta_liin(e, isa, s) or väljasta_liin(e, ema, s)
        if tõeväärtus:
            print(j)
        return tõeväärtus

    else:
        return False
#     if e==j:
#         return True
#     if e in sõnastik[j]:
#         return True
#     else:
#         for el in sõnastik[j]:
#             print(fun(e, el))
#         for nimi in sõnastik:
#             if e in sõnastik[nimi]:
#                # print(nimi)
#                 fun(nimi, j)
                    
print("Kas liin leidub?",väljasta_liin('Mari','Kalle' , sõnastik)) 
    
    
    
    
    
    
    
    