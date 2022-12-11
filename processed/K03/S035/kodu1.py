a=float(input("Sisesta aastatulu: "))
while a<0:
    a=float(input("Sisesta aastatulu: "))
if a<=6000:
    print (a)
elif 6000<a<=14400:
    print("6000")
elif 14400<a<=25200:
    print(round(6000 - (6000 / 10800) * (a - 14400), 2))
elif a>25200:
    print(0)

