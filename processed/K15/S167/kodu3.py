import re

#nimi = input("Sisesta failinimi:")

f = open("sõiduplaan.txt", "r")

jar1 = []
for i in f:
    a = i.strip().split()
    jar1.append(a)

def saabumisaeg(jar1):
    for i in range(len(jar1)):
        min = i
        for j in range(i+1, len(jar1)):
            if jar1[j][0] < jar1[min][0]:
                min = j
        if i != min:
            jar1[i], jar1[min] = jar1[min], jar1[i]
    return jar1

def väljumisaeg(jar1):
    for i in range(len(jar1)):
        min = i
        for j in range(i+1, len(jar1)):
            if jar1[j][1] < jar1[min][1]:
                min = j
        if i != min:
            jar1[i], jar1[min] = jar1[min], jar1[i]
    return jar1

def hind(jar1):
    for i in range(len(jar1)):
        min = i
        for j in range(i+1, len(jar1)):
            if jar1[j][2] < jar1[min][2]:
                min = j
        if i != min:
            jar1[i], jar1[min] = jar1[min], jar1[i]
    return jar1

   
if hind(jar1)[0] == saabumisaeg(jar1)[0] and saabumisaeg(jar1)[0] == väljumisaeg(jar1)[0]:
    d = hind(jar1).pop(0)
    print(d)
if hind(jar1)[0] == väljumisaeg(jar1)[0]:
    d = hind(jar1).pop(0)
    print(d)
if hind(jar1)[0] == saabumisaeg(jar1)[0]:
    d = hind(jar1).pop(0)
    print(d)
if väljumisaeg(jar1)[0] == saabumisaeg(jar1)[0]:
    d = väljumisaeg(jar1).pop(0)
    print(d)


# saabumisaeg(jar1)
# d = jar1.pop(0)
# print(d[0], d[1], d[2])
# 
# väljumisaeg(jar1)
# d = jar1.pop(0)
# print(d[0], d[1], d[2])
# 
# hind(jar1)
# d = jar1.pop(0)
# print(d[0], d[1], d[2])