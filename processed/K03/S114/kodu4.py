f = open("kinganumbrid.txt", encoding = "UTF-8")
read = f.readlines()
for rida in read:
    try:
        kinganumber = float(rida.strip())
        vastus = 2/3*(kinganumber-2)
        print(round(vastus))
    except:
        print("Vigane sisend")

f.close()