i=0
av = open("kinganumbrid.txt", "r")
rida = av.read()
kinganr = (rida.strip("\n").split())

while i < len(kinganr):
    try:
        pikkus = (round(2/3 *(float(kinganr[i])-2)))
        print(pikkus)
    except:
        print("Vigane sisend")
    i=i+1
