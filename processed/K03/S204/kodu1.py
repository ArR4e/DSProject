import math


a = float(input("Palun sisesta aastatulu: "))
b = float(a-14400)
c = float(6000-(5/9)*b)
d = str('6000')
e = str('0')
f = (".00")




if a < 0:
    print("Rike, palun sisesta positiivne arv: ")

elif 0 < a <=6000:
    print(round(a,2))
     
    
elif 6000< a <=14400:
    print(d+f)

elif 14400< a <=25200:
    print(round(c,2))
elif a > 25200:
    print (e+f)
    



    
    

    

    
    

