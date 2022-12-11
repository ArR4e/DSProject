n=int(input("Sisestage naturaalarv: "))
allSum=(n*(n+1)//2)
def squaresum(n) :
    sm = 0
    for i in range(1, n+1) :
        sm = sm + (i * i)
      
    return sm
a=squaresum(n)-allSum
#print(allSum)
#print(squaresum(n))
print(a)
#https://www.geeksforgeeks.org & https://stackoverflow.com