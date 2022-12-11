
teepikkus = float(input("Sisestage tee pikkus koju kilomeetrites: "))

f = open("taksohinnad.txt", encoding = "UTF-8")

for rida in f:
    t = rida.split()
    stardihind = float(t[1])
    km_hind = float(t[2])
    hind = stardihind + km_hind * teepikkus
    hind.append()
print(hind)
# t1 = f.readline().split(",")
# t2 = f.readline().split(",")
# t3 = f.readline().split(",")
# 
# hind_t1 = float(t1[1]) + teepikkus * float(t1[2])
# hind_t2 = float(t2[1]) + teepikkus * float(t2[2])
# hind_t3 = float(t3[1]) + teepikkus * float(t3[2])
# 
# hinnad = hind_t1.append(hind_t2, hind_t3)
# 
# nimed.append(t1[0], t2[0], t3[0])
# 
# indeks = 0
# miinimum = järjend[0]
# for i in range(len(järjend)):
#     if järjend[i] < miinimum:
#         miinimum = järjend[i]
#         indeks = i
# 
# print(hind_t1)

# takso1 = t1.split()
# takso2 = t2.split()
# takso3 = t3.split()
# 
# print(takso2)
# hind1 = takso1[1] + takso1[2] * teepikkus
# hind2 = takso2[2] + takso2[3] * teepikkus
# hind3 = takso3[2] + takso3[3] * teepikkus
# 
# if hind1 < hind2 and hind1 < hind3:
#     print(takso1[0])
# if hind2 < hind1 and hind2 < hind3:
#     print(takso2[0] + takso2[1])
# if hind3 < hind1 and hind3 < hind2:
#     print(takso3[0] + takso3[1])

# print(takso1[2])
# print(takso2[3])
# print(takso3[3])
#     
f.close()

#fail taksohinnad.txt:
#failis on kirjas:
    #taksode nimi, sisseistumise hind, kilomeetri hind (komadega eraldatud)
#Programm küsib kasutajalt:
    #tee pikkuse koju km-s
#Programm väljastab(vastavalt faili hindadele):
    #kõige odavama takso nimi