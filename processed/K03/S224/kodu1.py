x = float(input("Sisesta aastatulu "))

if x > 0 and x < 6000:
    print("Maksuvaba tulu on võrdne aastatuluga ehk "+ str(x))
    
if x > 6000 and x < 14400:
    print("Maksuvaba tulu on 6000 eurot aastas")
    
if x > 14400 and x < 25200:
    y = 6000 - (6000 / 10800) * (x - 14400)
    print("Maksuvaba tulu on " + str(round(y, 2)))
    
if x > 25200:
    print("Maksuvaba tulu on 0 eurot")
    
else:
    print("Ei saa olla negatiivne")
    
    