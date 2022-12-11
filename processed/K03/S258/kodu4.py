w = open("kinganumbrid.txt")
lopp = ""

while True:
    rida = w.readline().strip()
    if rida!="":
        try:
            lopp+=str(round( 2*(float(rida)-2)/3))+ "\n"
        except:
            lopp+="Vigane sisend\n"
    else:
        break
print(lopp.strip())


