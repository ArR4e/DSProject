n_algne = int(input("Sisesta naturaalarv: "))

n = n_algne
ruutude_summa = 0
summa_ruut = 0

if n <= 0:
    print("See pole naturaalarv.")

else:
    while n >= 1:
        n_ruudus = n**2
        ruutude_summa += n_ruudus
        n -= 1

n = n_algne

while n != 0:
    summa_ruut += n
    n -= 1
    if n == 0:
        summa_ruut = summa_ruut ** 2

vahe = summa_ruut - ruutude_summa

print(vahe)