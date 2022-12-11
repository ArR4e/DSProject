fail = input("Sisesta failinimi:")

f = open(fail, encoding = 'utf-8')

buses = []

indeces_to_remove = []

for row in f:
    parts = row.strip().split()
    time = parts[0], parts[1]
    price = parts[2]
    bus = time, price
    buses.append(bus)
f.close()
    
for i in range(len(buses) - 1):
    for j in range(i + 1, len(buses)):
        if buses[j][0][0] < buses[i][0][0]:
            buses[j], buses[i] = buses[i], buses[j]
            
for i in range(len(buses) - 1):
    for j in range(i + 1, len(buses)):
        if buses[i][0][1] > buses[j][0][1]:
            if int(buses[i][1]) > int(buses[j][1]):
                indeces_to_remove.append(i)
    


print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")

for i in range(len(buses)):
    if i not in indeces_to_remove:
        print(buses[i][0][0], buses[i][0][1], buses[i][1])
  