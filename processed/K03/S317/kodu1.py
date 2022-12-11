a = input("Sisesta oma aastatulu: ")
b = float(a)
aastatulu = abs(b)
if aastatulu <= 6000:
    print("Aastatulu on võrdne maksuvaba tuluga ehk ", aastatulu, "eurot")
else: 
    if aastatulu > 6000 and aastatulu <= 14400:
        print("Maksuvaba tulu on 6000 eurot")
    else:
        if aastatulu > 14400 and aastatulu <= 25200:
            aastatuluarv = 6000 - ((6000/10800)*(aastatulu-14400))
            print("Maksuvaba tulu on ", round(aastatuluarv, 2), "eurot")
        else:
            if aastatulu > 25200:
                print("Maksuvaba tulu on 0 eurot")
            