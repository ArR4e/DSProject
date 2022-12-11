tulu = float(input("Mis su aastatulu on kah? "))
s = 0.00

if tulu < 6000:
    s += tulu
elif 6000 <= tulu < 14400:
    s += 6000
elif 14400 <= tulu < 25200:
    s = 6000 - 6000 / 10800 * (tulu - 14400)
else:
    s = 0
    
s = round(s, 2)

print("Maksuvaba tulu on " + str(s))