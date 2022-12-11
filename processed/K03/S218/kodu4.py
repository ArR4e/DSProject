f = open("kinganumbrid.txt")

while True:
    number= f.readline()
    
    if number== "":
        break
    
    try:
        number_oige = float(number)
        print(round(2/3*(number_oige-2)))
        
        
    except:
        print("Vigane sisend")
    
    
   
f.close()


