a = float(input("Sisesta aastatulu:"))
b = float(6000)
c = float(14400)
d = float(25200)
e = float(0)

if a <= b and a > e:
    print(float(a))
else:
    if a > b and a <= c:
        print(b)
    else:
        if a > c and a <= d:
            print(round((6000 - (6000/10800) * (a - 14400)), 2))
        else:
            if a > d:
                print(e)