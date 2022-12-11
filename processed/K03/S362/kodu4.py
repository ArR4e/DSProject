f=open("kinganumbrid.txt")

while True:
    try:
        
            
        kinganumber=f.readline()
        if kinganumber=="":
            break
        pikkus=2/3*(float(kinganumber)-2)
        print(round(pikkus))
            
    except:
        print("Vigane sisend")
        

        
        
        
            
        
    

f.close()