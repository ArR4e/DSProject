vahemik = int(input('Sisesta naturaalarv'))
arv = range(0, vahemik + 1)
summaruut = (sum(arv)) ** 2

#Leidsin inspiratsiooni codershubb.com -st
sum = 0
while vahemik > 0:
    sum = sum + (vahemik*vahemik)
    vahemik = vahemik-1
vastus = summaruut - sum
print('Summaruudu ja ruutude\n summa vahe on ', vastus)