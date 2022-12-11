f=open('kinganumbrid.txt.')
lines=f.readlines()
i = 0
while i > (-1):
    if (lines[i]).isalpha() == True:
        print('Vigane sisend')
        else:
            print(round(((lines[i])-2) *   2/3 ))
    i +=1
f.close()
    
    
    
    

