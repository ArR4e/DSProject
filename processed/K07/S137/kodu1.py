def poisse_ja_tüdrukuid(andmed):
    poisid = tüdrukud = a = 0
    for i in andmed:
        for täht in i:
            if täht == ' ':
                a = 1
            if a ==1 and täht == 'P':
                poisid = poisid + 1
                a = 0
            if a == 1 and täht == 'T':
                tüdrukud = tüdrukud + 1
                a = 0
    ennik = (poisid,tüdrukud)
    return ennik
aff = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']    
x = poisse_ja_tüdrukuid(aff)
print(x)