f=open("king.txt")

n=int(input("Sisesta mitu jalanõu numbrit fail sisaldab: "))
i=0

while i<n:
    try:
        m=float(f.readline().strip())
        a=round(2/3*(m-2),2)
        print(a)
    except:  
        print("Vigane sisend")
       
    i+=1
f.close()
    
    
    
    

