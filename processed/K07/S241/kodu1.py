a = ['Mati P', 'Kati T', 'Malle T', 'Kalle P', 'Jüri P', 'Mari T']

def poisse_ja_tüdrukuid(j):
    summa_p=0
    summa_t=0
    for e in j:
        if e[-1] == "P":
            summa_p +=1
        else:
            summa_t += 1
    return summa_p, summa_t
print(poisse_ja_tüdrukuid(a))

