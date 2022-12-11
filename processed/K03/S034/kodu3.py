#küsin kasutaja käest ühe naturaalarvu.
n = int(input("Palun sisesta naturaalarv n: "))

#Teeme kindlaks, kas sisestatud arv on ikkagi naturaalarv ehk kas see on suurem või võrdne nulliga.
if n < 0:
    print("Sisestatud arv pole naturaalarv. Proovi arve 0, 1, 2, 3, ... jne.")

elif n >= 0:    
# vaadeldav naturaalarv on n.


#esimese n arvu summa leiame valemiga (n*(n+1)/2)
#Leiame esimese n naturaalarvu summa ruudu:
    summa_ruut = int((n*(n+1)/2)**2)


#Leiame esimese n naturaalarvu ruutude summa:
    ruutude_summa = 0
    for n in range (1, n+1):
        ruutude_summa = ruutude_summa + (n*n)

    
#Leiame esimese n naturaalarvu summa ruudu ja ruutude summa erinevuse:
    lahend = str(summa_ruut - ruutude_summa)
    print("Esimese " + str(n) + " naturaalarvu summa ruudu ja ruutude summa erinevus on " + lahend + "." )