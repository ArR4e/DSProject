aastatulu = float(input("Sisestage aastatulu: "))

if(aastatulu  < 6000.0):
    print("Maksuvaba tulu on ", aastatulu, "eurot")

elif(6000.0 <= aastatulu < 14400.0):
    print("Maksuvaba tulu on 6000 eurot")

elif(14400.0 <= aastatulu < 25200.0):
    print("Maksuvaba tulu on ", round((6000-6000/10800*(aastatulu-14400)), 2), "eurot")

elif(aastatulu >= 25200.0):
    print("Maksuvaba tulu on 0 eurot")