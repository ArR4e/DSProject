n = int(input("Mitu naturaalarvu? "))

def ruutsumma (n):
    summa = 0
    i = 1
    while i <= n:
        summa +=i*i
        i = i+1
    return summa

def summaruut (n):
    summa = 0
    i = 1
    while i <= n:
        summa = summa+i
        i = i+1
    return summa*summa

vastus = summaruut(n)-ruutsumma(n)
print(vastus)

        
    