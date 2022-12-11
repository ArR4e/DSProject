def moos(s,v,k):
    summa=0
    while k>=5 and s>0:
        k=k-5
        s-=1
        summa+=1
    while k>0:
        if v>0:
            k=k-1
            v-=1
            summa+=1
        else:
            return (-1)
    return (summa)
s= int(input("Kui palju on suuri karpe? "))
v= int(input("Kui palju on väikseid karpe? "))
k= int(input("Mitu liitrit moosi? "))
moos(s,v,k)            