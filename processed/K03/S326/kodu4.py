f = open("kinganumbrid.txt")
while True:
    nr = f.readline()
    if nr == "":
        break
    try:
        jala_pikkus = round(2/3*(float(nr)-2))
        print(jala_pikkus)
    except:
        print("Vigane sisend")
f.close()