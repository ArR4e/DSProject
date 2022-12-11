bruto=float(input("Sisesta aastatulu: "))
if bruto <= 6000:
    print("Maksuvaba tulu on " + str(bruto))
elif bruto>6000 and bruto<=14400:
    print("Maksuvaba tulu on 6000")
elif bruto>14400 and bruto<=25200:
    print("Maksuvaba tulu on " + str(round(6000-(6000/10800*(bruto - 14400)), 2)))
elif bruto>25200:
    print("Maksuvaba tulu on 0")