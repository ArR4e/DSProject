n = int(input("Sisestage naturaalarvu: "))
a=1
rs=0
sr=0
while a<=n:
    rs += a**2
    sr += a
    a+=1
print((sr**2)-rs)