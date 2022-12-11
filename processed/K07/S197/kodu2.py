f = open('taksohinnad.txt', encoding='utf-8')
line = f.readline()

km = float(input('Sisesta tee pikkus kilomeetrites: '))
cheapest_name = ''
cheapest_price = 0

while line:
    line_elements = line.split(',')
    price = float(line_elements[1]) + km * float(line_elements[2])
    if cheapest_price == 0 or cheapest_price > price:
        cheapest_name = line_elements[0]
        cheapest_price = price
    line = f.readline()

f.close()
print(f'Kõige odavam on {cheapest_name}.')