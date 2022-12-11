def poisse_ja_tüdrukuid(järjend) :
    m=0
    n=0
    for element in järjend:
        sugu= element[-1] #teame,et sugu on viimasel positsioonil olev täht
        if sugu=='P':
            m+=1
        elif sugu== 'T':
            n+=1
        
    return (m,n)   

#print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))
