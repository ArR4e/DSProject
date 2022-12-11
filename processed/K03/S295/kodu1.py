m = float(input("Sisesta aastatulu:"))
m2 = round(m, 2)
if m2 < 6000:
    print ("Maksuvaba tulu on", m2, "eurot.")
elif 6000 <= m2 and m2 <= 14400:
    print("Maksuvaba tulu on 6000 eurot.")
elif 14400 <= m2 <= 25200:
    n = 6000 - (6000/10800*(m2-14400))
    n2 = round(n, 2)
    print("Maksuvaba tulu on", n2, "eurot.")
elif m2 > 25200:
    print("Maksuvaba tulu: on 0 eurot.")
        
    
    