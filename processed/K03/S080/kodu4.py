f = open('kinganumbrid.txt')
loe = f.read()
b=loe.count('\n')
f.close()
c = open('kinganumbrid.txt')
i = 0
d=0
while i+d<=b:
    try:
        #d-1
        rida=float(c.readline())
        print(round(2/3*(rida-2)))
        i=i+1

    except:
        print('Vigane sisend')
        d=d+1
d=d-1

        


f.close()
