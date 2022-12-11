a = ['Kati T', 'Veronika T', 'Peeter T']

def poisse_ja_tüdrukuid(a):
    m = 0
    n = 0
    
    for i in a:
        if ' P' in i:
            m += 1
        if ' T' in i:
            n += 1
    return (m, n)

print(poisse_ja_tüdrukuid(a))