tulu = float(input("Sisestage oma aastane tulu: "))

if(tulu < 0):
    print("Tulu ei saa olla negatiivne!")
elif(tulu <= 6000):
    tulu = round(tulu, 2)
    print("Teie maksuvaba tulu määr on ", tulu)
elif(tulu <= 14400):
    print("Teie maksuvaba tulu määr on 6000")
elif(tulu <= 25200):
    uustulu = 6000-6000/10800*(tulu - 14400)
    uustulu = round(uustulu, 2)
    print("Teie maksuvaba tulu määr on ", uustulu)
elif(tulu > 25200):
    print("Teie maksuvaba tulu määr on 0")