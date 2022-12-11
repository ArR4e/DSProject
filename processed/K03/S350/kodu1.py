a=float(input("Aastatulu: "))
b=6000-6000/10800*(a-14400)
if a<0:
    print("Aastatulu ei saa olla negatiivne")
elif a>=25200:
    print("Maksuvaba tulu on 0 eurot")
elif 6000<=a<14400:
    print("Maksuvaba tulu on 6000 eurot aastas")
elif a<6000:
    print("Maksuvaba tulu on " + str(a) + " eurot")
elif 14400<=a<25200:
    print("Maksuvaba tulu on "+str(round(b,2)))
    