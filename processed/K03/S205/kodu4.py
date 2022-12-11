f = open('kinganumbrid.txt')
for line in f:
    try:
        a=float((line))
        print(round((float(line)-2)*2/3))
    except:
        print('Vigane sisend')

f.close()