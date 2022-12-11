sisend=float(input("Sisestage enda aastatulu:"))
vaba=0
if sisend <=6000:
    vaba=sisend
elif sisend < 14400:
    vaba=6000
elif sisend > 25200:
    vaba=0
else:
    vaba=6000-6000/10800*(sisend-14400)
valja = round(vaba,2)
valja=str(valja)
print("Maksuvaba tulu on "+valja+" eurot.")
    