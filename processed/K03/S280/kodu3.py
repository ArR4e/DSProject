# 3. Ruudud / RP

n = 0
rs = 0
sr = 0
arv = int(input("Sisesta naturaalarv: "))

while n <= arv:
    rs += n ** 2
    sr += n 
    n += 1
sr = sr ** 2
print("Ruutude summa on: " + str(rs))
print("Summa ruut on: " + str(sr))
print("Nende erinevus on " + str(sr-rs) + ".")