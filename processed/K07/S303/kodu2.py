taxi_lists = []
prices_list = []
cheapest = ''

with open('taksohinnad.txt') as f:
    for line in f:
        taxi_lists.append(line.strip().split(','))
        
road_length = float(input('Enter a road length in km: '))

for t_list in taxi_lists:
    prices_list.append(float(t_list[1]) + float(t_list[2]) * road_length)
    
if taxi_lists: cheapest = taxi_lists[prices_list.index(min(prices_list))][0]

print(f'Most cheap taxi is {cheapest}')
