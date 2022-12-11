atulu = float(input("Sisesta aastatulu: "))
if 0 <= atulu <= 6000:
    print("Maksuvaba tulu on", round(atulu, 2), "eurot.")
elif 6000 < atulu <= 14400:
    print("Maksuvaba tulu on 6000 eurot.")
elif 14400 < atulu <= 25200:
    mtulu = 6000 - 6000 / 10800 * (atulu - 14400)
    print = print("Maksuvaba tulu on", round(mtulu, 2), "eurot.")
elif 25000 < atulu:
    print("Maksuvaba tulu on 0 eurot.")
else:
    print("Viga arv")
