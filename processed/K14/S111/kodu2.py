n= int(input("Sisest arvu n väärtus: "))
a=n
summa=0
arv=0
while n>0:
    rs=n**2
    summa=rs + summa
    arv=a+arv
    a=a-1
    n=n-1
arv=arv**2
print(arv-summa)

