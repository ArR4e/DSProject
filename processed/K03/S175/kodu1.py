aastatulu = input("Sisesta aastatulu: ")
aastatulu1 = float(aastatulu)
aastatuluUmardus = round(aastatulu1, 2)
aastatulukesk = round(6000- 6000 / 10800 * (aastatulu1 - 14400), 2)




if aastatulu1 > 25200:
    print("Maksuvaba tulu on 0 eurot.")
else:
    if aastatulu1 >= 14400 and aastatulu1 <= 25200:
            print("Maksuvaba tulu on ", aastatulukesk)
    else:
        if aastatulu1 >= 6000 and aastatulu1 <= 14400:
            print("Maksuvaba tulu on ",  round(6000, 0), "eurot.")
        else:
            if aastatulu1 <= 6000:
                print("Maksuvaba tulu on ", aastatuluUmardus, "eurot.")

        
                  
                 
   
   