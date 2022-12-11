arv = int(input("Sisestage palun üks arv: " ))
i = 1
summa = 0
ruut = 0
while i <= arv:
    summa += i 
    ruut += i ** 2
    i += 1
    
tulemus = summa ** 2 - ruut
print (tulemus)