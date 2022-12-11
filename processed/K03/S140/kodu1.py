atulu = float(input("Sisestage oma aastatulu: "))

if atulu >= 0:
    if atulu <= 6000:
        print("Teie tulust on maksuvaba " + str(atulu) + "€")
    elif atulu <= 14_400:
        print("Teie tulust on maksuvaba 6000€")
    elif atulu <= 25_200:
        maksvaba = 6000 - 6000 / 10800 * (atulu - 14400)
        print("Teie tulust on maksuvaba " + str(round(maksvaba, 2)) + "€")
    else:
        print("Teie tulust on maksuvaba 0€")
else:
    print("Pidite sisestama positiivse arvu!")
    