with open(input('Sisesta failinimi: '), 'r', encoding='utf-8') as f:
    plan = f.read().splitlines()

subpar=[]
for i in range(len(plan)):
    bus_a = plan[i].split(' ')
    for j in range(len(plan)):
        bus_b = plan[j].split(' ')
        if bus_a[0] < bus_b[0] and bus_a[1] > bus_b[1] and float(bus_a[2]) > float(bus_b[2]):
            subpar.append(plan[i])
            break

print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:')
print(*sorted([bus for bus in plan if bus not in subpar]), sep='\n')