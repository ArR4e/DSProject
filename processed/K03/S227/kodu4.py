f=open("kinganumbrid.txt")

while True:
    line=f.readline().strip()
    if not line:
        break
    try:
        print(round(2/3*((float(line))-2)))
    except:
        print("Vigane Sisend")
f.close