# ei mõista miks automaat kontroll ei mõista seda

f = open("Kinganumbrid.txt", 'r')

numbrid = [line.strip() for line in f]

for i in numbrid:
    try:
        print(round(2/3*(float(i)-2)))
    except:
        print("vigane sisend")

f.close()
