arv = float(input("Sisesta oma aastatulu: "))
maksuvabatulu = (6000- (6000 / 10800) * (arv - 14400))
ümardatud = round(maksuvabatulu, 2)
if arv < 0:
    print("Palun sisesta aastatulu ehk positiivne arv: ")

elif arv < 6000:
    print("Maksuvaba tulu on " + str(round(arv, 2)) + " " + "eurot")
elif arv < 14400:
    print("Teie maksuvaba tulu on 6000 eurot")
    
elif arv < 25200:
    print("Teie maksuvaba tulu on " + str(ümardatud))
    
elif arv > 25200:
    print("Teie maksuvaba tulu on 0 ")