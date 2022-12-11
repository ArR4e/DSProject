aastatulu = float(input("Sisesta aastatulu: "))

if aastatulu <= 6000:
    print("Maksuvaba tulu on",round(aastatulu, 2))
    
elif aastatulu > 6000 and aastatulu <= 14400:
    uus_arv = (aastatulu - 6000)*0.2
    print("Maksuvaba tulu on",round(uus_arv, 2))

elif aastatulu > 14400 and aastatulu <= 25200:
    uus_arv = 6000-6000/10800*(aastatulu-14400)
    print("Maksuvaba tulu on",round(uus_arv, 2))

else:
    print("Maksuvaba tulu on 0")