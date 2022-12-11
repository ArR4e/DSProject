n=int(input("Sisesta mitu esimest naturaalarvu võtta: "))
l=n
if n < 0:
    print("Sisesta positiivne arv!")
elif n > 0:
   sum = 0
   while(n > 0):
       sum += n
       n -= 1
       b=sum*sum
       sumR = 0
       for i in range(1, l+1):
           sumR += (i*i)
   print("Esimese "+str(l)+" naturaalarvu summa ruudu ja ruutude summa erinevus on "+str(b-sumR)+".")
elif n == 0:
    print("Esimese 0 naturaalarvu summa ruudu ja ruutude summa erinevus on 0.")