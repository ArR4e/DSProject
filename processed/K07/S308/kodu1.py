järjend = (['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])
def poisse_ja_tüdrukuid(järjend):
    m=0
    n=0
    for isik in järjend:
        #isik.split(' ')
        if isik[-1]=='P':
            m+=1
        elif isik[-1]=='T':
            n+=1
        else:
            return(0)
    return(m,n)
print(poisse_ja_tüdrukuid(järjend))