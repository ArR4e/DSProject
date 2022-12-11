f = open("kinganumbrid.txt", encoding = 'UTF-8')
a = f.readline()
b = f.readline()
c = f.readline()
d = f.readline()
try:
    a2 = round(2/3 * (float(a) - 2))
    print(a2)
except:
    print("Vigane sisend")
try:
    b2 = round(2/3 * (float(b) - 2))
    print(b2)
except:
    print("Vigane sisend")
try:
    c2 = round(2/3 * (float(c) - 2))
    print(c2)
except:
    print("Vigane sisend")
try:
    d2 = round(2/3 * (float(d) - 2))
    print(d2)
except:
    print("Vigane sisend")
f.close()