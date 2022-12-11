def transponeeri(maatriks):
    for i in range(2,-1,-1):
        for j in range(1,-1,-1):
            print(maatriks[j][i], end = " ")
        print()
järjend = []
def transponeeriK(maatriks):
    f = open("maatriks.txt", "w")
    f.write(transponeeri(maatriks))
    for rida in f:
        if rida == "":
            break
        järjend.append(rida)
    return(järjend)
    f.close()