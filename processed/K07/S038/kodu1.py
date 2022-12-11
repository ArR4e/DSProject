L=['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']

def poisse_ja_tüdrukuid(a):
    m = 0
    n = 0
    for element in a:
        uus= element.split(" ")
        if uus[-1] == "T":
            n += 1
        if uus[-1] == "P":
            m += 1
        else:
            continue
    return (m,n)

print(poisse_ja_tüdrukuid(L))
            
        
        
    
    
    
    