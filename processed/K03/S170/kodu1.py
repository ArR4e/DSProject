a = float(input("Sisesta aastatulu: "))
while a < 0:
    a = float(input("Palun sisestage positiivne arv: "))


if a <= 6000:
    print ("Maksuvaba tulu on", round(a, 2), "eurot.")
elif 6000 < a <= 14400:
    print ("Maksuvaba tulu on 6000 eurot.")
elif 14400 < a <= 25200:
    a = a - 14400
    l = 6000 / 10800
    b = l * a
    c = 6000 - b
    print ("Maksuvaba tulu on", round(c, 2), "eurot.")
elif 25200 < a:
    print ("Maksuvaba tulu on 0 eurot.")
