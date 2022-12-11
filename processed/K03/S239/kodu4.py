f=open("kinganumbrid.txt")

while True:
    kinga_nr=f.readline()
    if kinga_nr=="":
        break
    try:
        kinganr=float(kinga_nr)
        print(round(2/3*(kinganr-2),2))
    except:
        print("Vigane sisend.")