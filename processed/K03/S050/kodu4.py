f = open("kinganumbrid.txt")
p=f.readline()
while p:
    try:
        labap=2/3*(float(p)-2)
        print(round(labap))
        
    except:
        print('Vigane sisend')
    p=f.readline()
    
f.close()
     
        
    
