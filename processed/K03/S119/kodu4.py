b = open("kinganumbrid.txt", "r")
rida_on = True
while rida_on:
    rida = b.readline()
    if (rida ==""):
        break
    try:
        g = round((1.5 * float(rida) + 2))
        print(g)
    except:
        print("Vigane sisend")
b.close()