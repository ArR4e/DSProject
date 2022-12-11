import datetime

file = input('Sisesta failinimi: ')

schedule = []

top_price = 0
top_price_indices = []

top_time = datetime.datetime.strptime('', '') - datetime.datetime.strptime('', '')
top_time_indices = []

with open(file) as f:
    for line in f:
        schedule.append(line.split(' '))

for i in range(len(schedule)):
    price = int(schedule[i][2])
    if price > top_price:
        top_price = price
        top_price_indices = []
        top_price_indices.append(i)
    elif price == top_price:
        top_price_indices.append(i)
        
    
for i in range(len(schedule)):
    time = datetime.datetime.strptime(schedule[i][1], '%H:%M') - datetime.datetime.strptime(schedule[i][0], '%H:%M')
    if time > top_time:
        top_time = time
        top_time_indices = []
        top_time_indices.append(i)
    elif time == top_time:
        top_time_indices.append(i)

    
print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:')
for i in range(len(schedule)):
    if i in top_price_indices or i in top_time_indices:
        continue
    
    schedule[i][2] = schedule[i][2].strip()
    print(' '.join(schedule[i]))
    

