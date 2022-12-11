n = int(input("Sisestage naturaalarv: "))
def sq_sum(n):
    summa1=0
    summa2=0
    ind=0
    r=range(1,n+1)
    for i in r:
        summa1+=(i**2)
        summa2+=(i**2)
        for j in r[ind+1:]:
            summa1+=2*i*j
        ind+=1
    return summa1-summa2
print(sq_sum(n))