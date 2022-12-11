atulu = float(input("sisestage aastatulu: "))

tulu = 6000 - 6000/10800 * (atulu-14400)

if atulu<0:
    print("negatiivne aastatulu")
else:
    if atulu<6000:
        print("Maksuvaba tulu on", round(atulu,2) ,"eurot")
    elif atulu>=6000 and atulu<14400:
        print("Maksuvaba tulu on 6000.00 eurot")
    elif atulu>=14400 and atulu<25200:
        print("Maksuvaba tulu on", round(tulu,2) , "eurot")
    elif atulu>=25200:
        print("maksuvaba tulu on 0.00 eurot")
    else:
        print("viga")