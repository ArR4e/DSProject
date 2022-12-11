def poisse_ja_tüdrukuid(a):
    pois = 0
    tydr = 0
    
    for i in a:
        viimanetäht = i[-1]
        if viimanetäht == "P":
            pois += 1
        if viimanetäht == "T":
            tydr += 1
    punkt = (pois,tydr)
    return(punkt)
            
    
    
    

list1 = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']

poisse_ja_tüdrukuid(list1)