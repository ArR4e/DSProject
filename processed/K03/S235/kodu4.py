fail = open('kinganumbrid.txt', 'r')
read=fail.readlines()
ridade_arv=len(read)
fail.seek(0,0)
    
n=0
while n<ridade_arv:
    try:
        sisend=fail.readline()
        a=float(sisend)
        pikkus = round(2/3*(a-2))
        print(pikkus)
        n +=1               
    except:
        print("Vigane sisend")
        n += 1
   
fail.close()
    
    
