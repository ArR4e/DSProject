fail = open("kinganumbrid.txt")

while True:
    f = fail.readline()
    if f == "":
        break
    try:
        pikkus = 2/3 *(float(f)-2)
        pikkus = round(pikkus)
        print(pikkus)
    except:
        print("Vigane sisend")
        
fail.close()