x = float(input("Sisestage oma aastatulu eurodes: "))
if x < 0:
    print("Sisestage mittenegatiivne arv!")
elif x < 6000:
    print("Maksuvaba tulu on", round(x, 2), "eurot.")
elif x >= 6000 and x < 14400:
    print("Maksuvaba tulu on 6000 eurot.")
elif x >= 14400 and x < 25200:
    x= 6000-6000/10800*(x-14400)
    print("Maksuvaba tulu on", round(x, 2), "eurot.")
elif x >= 25200:
    print("Maksuvaba tulu on 0 eurot.")