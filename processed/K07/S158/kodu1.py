#järjend = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']
def poisse_ja_tüdrukuid(järjend) :
    poisid = 0
    tüdrukud = 0
    
    for i in järjend:
        if i[len(i)-1] == "P":
            poisid += 1
        else:
            tüdrukud += 1
            
    return (poisid, tüdrukud)
print(poisse_ja_tüdrukuid(järjend))