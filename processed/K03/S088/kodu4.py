f = open('kinganumbrid.txt')

while(True):
    king = f.readline()
    if king == "":
        break
    try:
        king = float(king.strip())
        cm = 2/3 * (king - 2)
        print(round(cm))
    except:
        print("Vigane sisend")

f.close()