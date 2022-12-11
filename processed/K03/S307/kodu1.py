tulu = float(input("Sisestage oma aastatulu"))
a = 6000
b = 14400
c = 25200
d = round(float(a - a/10800 * (tulu-14400)), 2)

if 0 <= tulu < a:
    print("Maksuvaba tulu on", tulu,  "eurot")
elif a <= tulu < b:
    print("Maksuvaba tulu on", a, "eurot")
elif b <= tulu < c:
    print("Maksuvaba tulu on", d, "eurot")
elif tulu >= c:
    print("Maksuvaba tulu on 0 eurot")
elif tulu < 0:
    print("Palun sisestage positiivne arv")
    
    
    