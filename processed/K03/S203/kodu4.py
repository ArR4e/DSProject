fail = open('kinganumbrid.txt', 'r')
read = fail.readlines()
ridade_arv = len(read)
fail.seek(0, 0)

n = 0
while n < ridade_arv:
    try:
        sisu = fail.readline()
        kas_on = float(sisu)
        tehe = 2/3 * (kas_on - 2)
        pikkus = round(tehe)
        print(pikkus)
        n += 1
    except:
        print("Vigane sisend")
        n += 1
    
        
    
        
        
    
        