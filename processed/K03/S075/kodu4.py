f=open("kinganumbrid.txt")

g=f.readline().strip()

while  g != "":
    try:
        print(str(round(2/3*(float(g)-2))))
    except ValueError:
        print("Vigane sisend")
    g=f.readline().strip()

f.close()