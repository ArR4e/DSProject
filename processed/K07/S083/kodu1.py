def poisse_ja_tüdrukuid(eesnimed):
    m=0
    n=0
    for x in eesnimed:
        if x[-1] == 'P':
            m+=1
        elif x[-1] == 'T':
            n+=1
        else:
            return 0 
    return (m, n)
            
eesnimed = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']
