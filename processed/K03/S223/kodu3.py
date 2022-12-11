def ruutudeVahe(n_arv):
    summa_ruut = 0
    ruutude_summa = 0
    for x in range(n_arv):
        ruutude_summa += (x+1)**2
    summa_ruut = (sum(range(0,n_arv+1,1))) ** 2
    return summa_ruut - ruutude_summa
viimane_arv = int(input("sisestaga n number: "))   
print(ruutudeVahe(viimane_arv))