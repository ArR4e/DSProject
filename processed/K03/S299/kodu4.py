f = open('kinganumbrid.txt')

nr1= f.readline()
nr2 = f.readline()
nr3= f.readline()
while True:
    try:
        laba1= round(2/3*nr1-2)
        laba2= round(2/3*nr2-2)
        laba3= round(2/3*nr3-2)
        print(laba1, laba2, laba3)
    except:
        print('Vigane sisend')
        
f.close()