aastatulu=float(input("Sisesta aastatulu: "))

if aastatulu <= 6000 :
    tulu=str(round(aastatulu, 2))
    print("Maksuvaba tulu on " + tulu + " eurot.")
if  6000 < aastatulu <= 14400 :
    print("Maksuvaba tulu on 6000.00 eurot.")
if 14400 < aastatulu <= 25200 :
    tulu=str(round(6000-6000/10800*(aastatulu-14400), 2))
    print("Maksuvaba tulu on " + tulu + " eurot.")
if 25200 < aastatulu :
    print("Maksuvaba tulu on 0.00 eurot.")

    
    