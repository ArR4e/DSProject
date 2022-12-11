palk=float(input("Sisesta oma aastatulu: "))
while palk <=0:
    palk=float(input("Sisesta oma aastatulu positiivse arvuna: "))
if palk <= 6000:
    print("Maksuvaba tulu on: "+str(round(palk,2))+" Eurot")
elif palk > 6000 and palk < 14400:
    print("Maksuvaba tulu on: "+"6000"+" Eurot")
elif palk > 14400 and palk < 25200:
    palk=6000-6000/10800*(palk-14400)
    print("Maksuvaba tulu on: "+str(round(palk,2))+" Eurot")
elif palk > 25200:
    print("Maksuvaba tulu on: "+"0"+" Eurot")