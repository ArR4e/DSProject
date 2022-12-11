f = open("kinganumbrid.txt", "r")
tekst = f.read()
x = tekst.split("\n")
read = len(x)
rida = 0
while read > rida:
    tex = x[rida]
    tex = tex.strip(" ")
    if tex.isnumeric():
        vastus = 2/3 * (float(tex) - 2)
        print(vastus)
    else:
        print("vigane sisend")
    rida += 1
