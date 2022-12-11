n = int(input("Sisesta naturaalarvu: "))
ruutude_summa = 0
ruut_summa = 0
i = 1
while i <= 10:
    ruut_summa += n
    n_ruut = n**2
    ruutude_summa += n_ruut
    n += 1
    i += 1
    
summade_erinevus = (ruut_summa)**2 - ruutude_summa
print(summade_erinevus)




    


    
    