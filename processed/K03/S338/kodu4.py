a = open("kinganumbrid.txt")
while True:
    b = a.readline()
    if b == "":
        break
    try:
        print(round((2/3)*(float(b)-2)))
    except:
        print("vigane sisend")