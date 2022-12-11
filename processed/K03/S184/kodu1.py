tulu_tekst=input("Sisesta aastatulu:")
tulu=float(tulu_tekst)
if tulu<=6000:
    vaba=tulu
if 6000<tulu<=14400:
    vaba=6000
if 14400<tulu<=25200:
    vaba=6000-(6000/10800)*(tulu-14400)
if tulu>=25200:
    vaba=0
vaba_lõpp=round(vaba,2)
print("Maksuvaba tulu on "+ str(vaba_lõpp)+" eurot.")