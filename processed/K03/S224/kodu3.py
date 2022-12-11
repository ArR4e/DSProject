x = int(input("Sisesta naturaalarv "))

if x <= 0:
    print("Ei sobi")
    
summa_ruut = (sum(range(1, x + 1)))**2



ruutude_summa = 0
for num in range(1, x + 1):
    ruutude_summa += (num*num)

print(summa_ruut - ruutude_summa)


    



