f = open("kinganumbrid.txt")
i=0
while i <4:
    a = f.readline()
    if a.replace("\n", "").replace(" ", "").isnumeric():
        x= 2/3*(float(a)-2)
        print(round(x))
    elif "." in a:
        x= 2/3*(float(a)-2)
        print(round(x))
    else:
        print("Vigane sisend!")
    i+=1

f.close()