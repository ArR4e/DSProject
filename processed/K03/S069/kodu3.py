n = int(input("Sisestage naturaal arv n: "))
i = 1
k = 0
j = 0
if(n < 0):
    print("Sisestage naturaal arv")
else:
    while(i <= n):
        k = k + pow(i, 2)
        j = j + i   
        i = i + 1

    j = j**2
    u = j - k
    print("Teie valitud arv oli", n, " ja tulemus on ", u)

    
    

    