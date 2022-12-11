tulu = int(input("Sisesta aastatulu: "))
if(tulu<=6000):
    print("Maksuvaba tulu on",tulu,"eurot.")
if(tulu>6000 and tulu<=14400):
    print("Maksuvaba tulu on 6000 eurot.")
if(tulu>14400 and tulu<25200):
    vaba = 6000 -(6000/10800* (tulu -14400))
    vaba = round(vaba, 2)
    print("Maksuvaba tulu on",vaba, "eurot.")
if(tulu>=25200):
    print("mitte sentigi")