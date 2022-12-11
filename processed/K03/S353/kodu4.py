#from time import sleep
f = open("kinganumbrid.txt", encoding='UTF-8')
while True: 
    try:
        stopper=str(f.readline())
        if stopper=='':
            break
        x=round(2/3*(float(stopper)-2))
        print(x)
    except:
        print("Vigane sisend")
    #sleep(1)
    