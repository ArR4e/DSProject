f = open("kinganumbrid.txt")
while True :
    number = f.readline()
    if number == "":
        break
    while True :
        try:
            kinga_number = float(number)
            print(round(((2/3) *(kinga_number-2))))
        except:
            print("Vigane sisend")
            
        break
