king = read = ("kinganumbrid.txt")
read = open(read)
read = len(read.readlines())
king = open(king)
x = 0
while x<read:
    kinganumbrid = king.readline()
    x +=1
    try:
        suurus = float(kinganumbrid)
        suurus = (suurus-2) * 2/3
        suurus = round(suurus)
        print(suurus)
    except :
        print("vigane sisend")
king.close()