a = float(input("Sisesta aastatulu:"))
if a<=6000:
    print(round(a, 2))
elif a>6000 and a<=14400:
    print(round(6000, 2))
elif a>14400 and a<=25200:
    print(round(6000-(6000/10800)*(a-14400), 2))
elif a>25200:
    print(0)