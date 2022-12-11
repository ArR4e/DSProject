a=open("kinganumbrid.txt", "r")

e=("a") 
while e!="":
    try:
        e=a.readline().strip("\n")
        if e=="":
            break
        if float(e) == round(float(e),1):
            print(int(round(2/3*(float(e)-2), 0)))
        else:
            print("Vigane sisend, liiga palju komakohti")
    
    except:
        print("Vigane sisend, pole arv")
         
    