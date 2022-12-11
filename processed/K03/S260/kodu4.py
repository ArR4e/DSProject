f = open("kinganumbrid.txt")

data = f.readlines()

for i in range(len(data)):
    try:
        print(round(2/3*(float(data[i].strip())-2)))
    except ValueError:
        print("Vigane sisend")