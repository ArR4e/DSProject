f = open("kinganumbrid.txt")

while True:
    kinganr = f.readline()
    
    if kinganr == "":
        break
    else:
        try:
            ümardus = round(float(kinganr))
            str(ümardus).isnumeric()
            print(round(2/3 * (float(kinganr) - 2)))
        except:
            print("Vigane sisend")

f.close()
    



