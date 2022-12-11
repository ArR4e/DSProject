sf=open('kinganumbrid.txt' ,'r')

for rida in sf:
    try:
        jalanumber=round(2/3*(float(rida.strip("\n"))-2))
        print(jalanumber)
    except:
        print("Vigane sisend")
    
