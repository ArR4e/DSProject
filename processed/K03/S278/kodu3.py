n = int(input("Tere! Palun sisesta naturaalne arv ja vajuta ENTER: "))
sum1 = 0
sum2 = 0
if n <= 0:
    print(0)
else:
    for s in range(1, n+1):
        sum1 = sum1 + (s*s)
        sum2 = sum2 + n
        squareSum2 = sum2**2
        n = n-1
        m = squareSum2-sum1
    print("Naturaalarvu summa ruut on", sum1, ". Erinevus on", m)

        