n=int(input("Sisesta naturaalarv: "))
x=1
y=1
summa=0
summaarum=0
while x <= n:
    a=x**2
    summa +=a
    x+=1
while y <= n:
    b=y
    summaarum +=b
    y+=1
print(summaarum**2-summa)