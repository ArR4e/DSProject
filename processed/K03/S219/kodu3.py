n = int(input("Sisesta naturaalarv n: "))

#Jada esimene liige
n1 = n - n + 1

#n naturaalarvu summa
summa = n*(n+1)/2

#summa ruut
summaruut = summa * summa

#ruutude summa
ruutsumma = (n*(n+1)*(2*n+1))/6

vastus = summaruut - ruutsumma

print(vastus)

