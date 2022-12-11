n = int(input('Sisestage arv: '))
i = 1
a = 1
kokku = 0
summa = 0

if n == 0:
    print('0')
else:
    while i <= n and a <= n:
        ArvuRuut = i** 2
        kokku += ArvuRuut 
        i += 1
        summa += a
        a += 1
        SummaRuut = summa**2
        vastus = SummaRuut - kokku
    print(vastus)
