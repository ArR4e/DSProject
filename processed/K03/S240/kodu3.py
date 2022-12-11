n = int(input("Sisesta arv: "))
i = 1
r_summa = 0
z = 0

while i <= n:
    r_summa += i**2
    z += i
    i += 1
    
    
s_ruut = z**2
vahe = s_ruut - r_summa
print ("Erinevus on: " + str(vahe))


