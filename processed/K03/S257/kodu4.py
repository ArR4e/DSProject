f1 = open("kinganumbrid.txt")

for i in f1.readlines():
    try:
        print(round(2*(float(i)-2)/3))
    except:
        print("Vigane sisend")
f1.close()