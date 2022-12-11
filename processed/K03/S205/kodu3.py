ruutude_summa = 0
summa = 0
while True:
    arv = input("Anna täisarv mille naturaalarvude summa ruudu ja ruutude summa erinevust soovid teada: ")
    try:
        arv = int(arv)
        n = 1
        while n <= arv:
            ruutude_summa += n*n
            summa += n
            n +=1
        else:
            break
    except ValueError:
        print("Mõtle mis on täisarv ja proovi uuesti!")
        continue
    
print("Summa ruudu ja ruutude summa erinevus on " + str((summa*summa)-ruutude_summa))
    