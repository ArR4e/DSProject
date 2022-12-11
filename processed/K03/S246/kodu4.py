f = open('kinganumbrid.txt')

x = 2 / 3
while True:
    try:
        n = f.readline().strip()
        if n == '':
            break
        m = float(n)
        kinganr = x * (m - 2)
        pikkus = round(kinganr)
        print(pikkus)
        
    except:
        print("Vigane sisend")

f.close()