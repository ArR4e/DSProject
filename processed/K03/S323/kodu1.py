# kuni 6000€ aastas on maksuvaba tulu võrdne aasta tuluga
# 6000 kuni 14 400€ on maksuvaba tulu 6000€ aastas
# 14 400 kuni 25 200€ on maksuvaba tulu valem 6000 - 6000 / 10 800 * (aastatulu - 14 400)
# kui 25,2k+ siis mv tulu pole

# at = aastatulu
# mv = maksuvaba tulu
at = float(input("Sisestage aastatulu: "))
mv = 0

if at <= 6000:
    #print("alla 6k v võrdne")
    mv = at

elif at <= 14400:
    #print("6k kuni 14,4k")
    mv = 6000
    
elif at <= 25200:
    #print("Alla 25,2k")
    mv = 6000 - 6000 / 10800 * (at - 14400)

elif at > 25200:
    #print("Üle 25,2k")
    mv = 0
    
print("Maksuvaba tulu on "+ str(round(mv, 2)))