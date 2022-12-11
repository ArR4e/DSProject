aastatulu=float(input("palun sisestage aastatulu "))
if aastatulu < 0:
    print("oled liiga vaene Eestis elamiseks")
    
elif aastatulu<=6000: 
    print("maksuvaba tulu on " + str(aastatulu))
    
elif aastatulu<=14400:
     print("maksuvaba tulu on 6000 eurot")
elif aastatulu <=25200:
    b=round(6000-6000/10800*(aastatulu-14400),2)
    print("maksuvaba tulu on " + str(b))
else:
    print("maksuvaba aastatulu puudub, ehk on " +str(0))