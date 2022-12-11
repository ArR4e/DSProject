f=open('kinganumbrid.txt')

while True:
    try:
        x=f.readline()
        if x=='':
            break
        else:
            print(round(2/3*(float(x)-2)))
    except:
        print('Vigane sisend')
f.close()