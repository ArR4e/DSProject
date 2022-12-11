f = open('kinganumbrid.txt', 'r')
read = f.readlines()

while True:
    read = f.readlines()
    if read == []:
        break;
    for jalatsiNr in read:
        jalatsiNr = read.strip()
        
        if jalatsiNr.isnumeric():
            number = int(jalatsiNr)
            pikkus = round(2/3*(number-2))
            print(pikkus)
        else:
            print("vigane sisend")
        
f.close()