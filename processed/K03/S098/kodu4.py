
myfile = open('kinganumbrid.txt')
next_line = str(myfile.readline())
while next_line != "":
     try:
        pikkus = round(2/3 * (float(next_line) - 2))    
        print(str(pikkus))
        next_line = myfile.readline()
     except:
         print("Vigane sisend")    
         next_line = myfile.readline()               
         if next_line != "":
             pikkus = round(2/3 * (float(next_line) - 2))
             print(str(pikkus))
             next_line = myfile.readline()
         else:
             break
