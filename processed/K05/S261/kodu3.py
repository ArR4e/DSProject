def moos(a,b,c):
    i=j=1
    x=0
    karp=[]
    while ((x+5)<=c)and(i<=a):
        x=5*i
        karp=karp+[1]
        i+=1
    while (x<c)and(j<=b):
        x+=1
        karp=karp+[1]
        j+=1
    if x==c:
        return sum(karp)
    else:        
        return -1
a=int(input('Sisesta suurte karpide arv:'))
b=int(input('Sisesta väikeste karpide arv:'))
c=int(input('Sisesta moosi kogus:'))

print(moos(a, b, c))

