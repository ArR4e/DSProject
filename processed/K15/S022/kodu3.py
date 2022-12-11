failinimi = input("Sisesta failinimi: ")
fail = open(failinimi, 'r')
a=[]
hinnad = []

for rida in fail:
    rida = rida.strip()
    rida = rida.split(' ')
    rida[2] = int(rida[2])
    hinnad.append(rida[2])
    d = []
    d.append(rida[2])
    d.append(rida[0])
    d.append(rida[1])
    a.append(d)

rida = []
for i in range(len(a)):
    for j in range(len(a)):
        if a[i][1] < a[j][1] and a[i][2] > a[j][2] and  a[i][0] > a[j][0]:
            rida.append(i)



rida.reverse()
#print(rida)
ha = -1
for number in rida:
    if number !=ha:
        a.pop(number)
    ha = number
#print(a)

for i in range(len(a)):
        min = i
        for j in range(i+1, len(a)):
            if a[j][1] < a[min][1]:
                min = j
        if i != min:
            a[i],a[min] = a[min],a[i]

print("Esimesest linnast teise sõitmiseks võiksid kaaluda busse: ")
for kolmik in a:
    print(kolmik[1], kolmik[2], kolmik[0])