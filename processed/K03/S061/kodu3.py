n = int(input("Sisesta naturaalarv:"))

nat_arvu_ruutude_summa = 0
nat_arvu_summa = 0

while n > 0:
    nat_arvu_ruutude_summa = nat_arvu_ruutude_summa + n**2
    nat_arvu_summa = nat_arvu_summa + n
    n -= 1
    if n == 0:
        nat_arvu_summa_ruut = nat_arvu_summa**2

erinevus = nat_arvu_summa_ruut - nat_arvu_ruutude_summa

print(nat_arvu_ruutude_summa)
print(nat_arvu_summa_ruut)
print(erinevus)