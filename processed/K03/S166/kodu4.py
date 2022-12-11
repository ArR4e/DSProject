f = open("kinganumbrid.txt","r")
a = 3
while a!="":
    try:
        a = f.readline()
        if a == "":
            break
        b = 2/3*(float(a)-2)
        print(round(b))
    except:
        print("Vigane sisend")