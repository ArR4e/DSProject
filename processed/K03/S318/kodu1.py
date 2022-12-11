at = float(input("Sisesta aastatulu: "))

if at < 0:
    print("Kas sisestasid ikka mittenegatiivse arvu?")
elif at < 6000:
    print("Maksuvaba aastatulu on "+str(at)+" eurot.")
elif at >= 6000 and at < 14400:
    print("Maksuvaba aastatulu on 6000 eurot.")
elif at >= 14400 and at < 25200:
    print("Maksuvaba aastatulu on "+ str(round(6000-6000/10800*(at-14400), 2))+" eurot.")
elif at >= 25200:
    print("Maksuvaba aastatulu on 0 eurot.")
else:
    print("Kas sisestasid ikka mittenegatiivse arvu?")
