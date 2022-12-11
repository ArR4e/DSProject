f = open("taksohinnad.txt", "r", encoding="UTF-8")
lines = f.read().splitlines()
f.close()

teepikkus = float(input('Sisesta tee pikkus kilomeetrites: '))
price_list = []
for x in lines:
    line = x.split(",")
    price = float(line[1])+float(line[2])*teepikkus
    price_list.append(price)

try:
    min_index = price_list.index(min(price_list))
    print("Kõige odavam on "+lines[min_index].split(",")[0])
except ValueError:
    print("Tühi hinnakiri")
    