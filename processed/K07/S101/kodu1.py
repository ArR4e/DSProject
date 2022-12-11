
def poisse_ja_tüdrukuid(x):
    T=0
    P=0
    for i in range(len(x)):
        
        if (x[i][(len(x[i])-1):len(x[i])])=="P":
            P+=1
        elif (x[i][(len(x[i])-1):len(x[i])])=="T":
            T+=1
        else:
            return(0)
    return(P,T)
    
poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])