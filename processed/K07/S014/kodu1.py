nimed=['kati T','liis-marii T', 'kardo mart P']


def poisse_ja_tüdrukuid(nimed):
    P=0
    T=0
    for nimi in nimed:
        nimi=nimi.split()
        if nimi[-1]=='P':
            P+=1
        if nimi[-1]=='T':
            T+=1
    return (P,T)

print(poisse_ja_tüdrukuid(nimed))