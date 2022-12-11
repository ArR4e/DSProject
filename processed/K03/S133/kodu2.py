aastatulu=int(input("palun sisestage aastatulu "))
if aastatulu < 0:
    print("oled liiga vaene Eestis elamiseks")
    
elif aastatulu<=6000:
    print("maksuvaba tulu on " + aastatulu)
    
elif aastatulu<=14400:
     print("maksuvaba tulu on 6000 eurot")
elif aastatulu <=25200:
     print("maksuvaba tulu on " + str(6000-6000/10800*(aastatulu-14400)))