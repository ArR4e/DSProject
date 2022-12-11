f=open('kinganumbrid.txt')
numbrid=[]
pikkus=0

for line in f:
    numbrid.append(line.strip())

for i in range(len(numbrid)):
    try:
        pikkus=2/3*(float(numbrid[i])-2)
        print(round(pikkus))
    except:
        print('Vigane sisend')