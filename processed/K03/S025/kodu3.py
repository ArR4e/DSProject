n = int(input('Sisesta naturaalarv: '))
summ = 0
ruut_summ = 0

if n == 0:
    print('Summa ruudu ja ruutude summa erinevus on', n)

else:
    while n >= 1:
        summ += n
        ruut = n ** 2
        n = n - 1
        summ_ruut = summ ** 2
        ruut_summ += ruut
    print('Summa ruudu ja ruutude summa erinevus on', summ_ruut - ruut_summ)