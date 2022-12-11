a = int(input("Sisestage naturaalarv n: "))
ruutude_summa = 0
b = 1
c = 1
summade_ruut = 0
erinevus=0

while c <= a:
    summade_ruut = summade_ruut + c
    c+=1
summade_ruut = summade_ruut **2

while a >= b:
    ruutude_summa = ruutude_summa + b**2
    b+=1
    
erinevus = summade_ruut - ruutude_summa

print(erinevus)
    