f = open('kinganumbrid.txt', 'r')

arr = f.readlines()

f.close()

for i in arr:
    try:
        print(round(2/3*(float(i.strip())-2)))
    except:
        print('Vigane sisend')