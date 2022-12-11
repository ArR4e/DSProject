file = open("kinganumbrid.txt", "r")
data = file.read().splitlines()
file.close()
for i in data:
    try:
        pikkus =  2/3 * (float(i) - 2)
        data[data.index(i)] = round(pikkus)
        
    except:
        data[data.index(i)] = "Vigane sisend"
[print(x) for x in data]