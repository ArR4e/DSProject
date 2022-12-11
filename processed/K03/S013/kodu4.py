f = open("kinganumbrid.txt")

read = f.readlines()

for rida in read:
    try:
        rida = float(rida.strip())
        print(round((rida - 2) * (2/3)))
    except:
        print("Vigane sisend")
