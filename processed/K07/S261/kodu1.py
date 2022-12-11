def poisse_ja_tüdrukuid(jarjend):
    poiss=0
    girl=0
    for laps in jarjend:
        if laps[-1]=='P':
            poiss+=1
        elif laps[-1]=='T':
            girl+=1
    return (poiss,girl)
    
    
jarjend=input('Sisesta järjend: ')
    
poisse_ja_tüdrukuid(jarjend)  
    