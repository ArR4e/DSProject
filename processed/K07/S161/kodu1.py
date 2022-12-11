järj= ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']
def poisse_ja_tüdrukuid(järj):
    t=0
    p=0
    x=0
    for el in järj:
        x=el.split(' ')
        if x[len(x)-1]=='T':
            t+=1
        elif x[len(x)-1]=='P':
            p+=1
    ennik= (p, t)
    return ennik
print(poisse_ja_tüdrukuid(järj))