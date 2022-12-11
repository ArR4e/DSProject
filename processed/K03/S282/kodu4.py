f=open('kinganumbrid.txt')
for el in f:
    try:
        print(round(2/3*(float(el.strip())-2)))
    except:
        print('Vigane sisend')
