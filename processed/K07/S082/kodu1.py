def poisse_ja_tüdrukuid(nimed):
    t = 0
    p = 0
    for a in nimed:
        sugu = a[-1]
        if sugu == 'P':
            p +=1
        if sugu == 'T':
            t +=1
    return (p, t)
        
print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'SIim Aleksander P', 'Jüri P', 'Veronika T']))
    
    