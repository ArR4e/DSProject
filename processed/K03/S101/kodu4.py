f=open('kinganumbrid.txt')
while True:

    try:
        sisu=(f.readline())
        if sisu== "":
            break
        sisu=float(sisu)
        print(round((sisu-2)*2/3))
        
    except:
        print("Vigane sisend")
        
    

    
f.close()

    