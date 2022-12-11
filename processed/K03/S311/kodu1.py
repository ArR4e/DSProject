aasta = float(input("Sisesta aastatulu: "))
vaba = 0
if aasta < 0:
    print("Sisestage palun positiivne arv!")
elif aasta <= 6000:
    vaba = aasta
elif aasta <=14400:
    vaba = 6000
elif aasta <= 25200:
    vaba = 6000-(6000/10800)*(aasta-14400)
else:
    vaba = 0
print("Teie maksuvabaks tuluks on ", round(vaba, 2),"eurot,")