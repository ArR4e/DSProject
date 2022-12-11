maatriks = []
def transponeeriK(maatriks):
    o=len(maatriks)
    p=len(maatriks[o-1])
        


    
    

    k=[]

    for i in range(p-1,-1,-1):
        t=[]
        for j in range(o-1,-1,-1):
            t.append(maatriks[j][i])
            
    
        k+=[t]
        
      
    return k

