n = int(input('sisestage naturaalarv: '))
on = n
ns = n
nr = n**2
while n != 0:
    n -= 1
    ns += n
ns2 = ns**2

while on != 0:
    on -= 1
    nr += on**2
vahe = abs(ns2 - nr)
print('naturaalarvude summa ruudu ning ruutude summa erinevus on ' + str(vahe))