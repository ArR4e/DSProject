fail = open('kinganumbrid.txt',"r")
line = len(fail.readlines())
fail.close()
fail = open('kinganumbrid.txt',"r")
i = 1
while(i <= line):
    j = fail.readline()
    try:
        j = float(j)
    except:
        j = j
    k = isinstance(j, (float, int))
    if(k > 0):
        j = 2/3*(j-2)
        j = round(j)
        print(j)
    else:
        print("vigane sisend")
    i = i + 1
fail.close()
        


        
