f = open("kinganumbrid.txt", encoding = "UTF-8")
jalalaba = 0
for nr in f:
    try:
        float(nr)
        jalalaba = round((2/3)*(float(nr)-2))
        print(jalalaba)
    except ValueError:
        print("Vigane sisend")
f.close()