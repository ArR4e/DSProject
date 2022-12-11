a = float(input("Sisestage aastatulu: "))

b = 6000 #aastatulu 6000-14400
c = 6000-6000/10800*(a-14400) #aastatulu 14400-25200
d = 0 #aastatulu >25200

if a < 6000:
    print("Maksuvaba tulu aastas on", a, "eurot.")
elif a >= 6000 and a < 14400:
    print("Maksuvaba tulu aastas on", b, "eurot.")
elif a >= 14400 and a <= 25200:
    print("Maksuvaba tulu on", round(c,2), "eurot.")
else:
    print("Maksuvaba tulu on", d, "eurot.")

    
