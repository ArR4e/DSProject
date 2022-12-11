palk = float(input("Sisestage teie aastatulu: "))

if 0 < palk < 6000:
    print("Te maksavaba talu ei maksa")

elif 6000 <= palk < 14400:
    print("Teie maksavaba tulu on 6000 eurot aastas")
    
elif 14400 <= palk < 25200:
    raha = round(float(6000 - 6000 / 10800 * (palk - 14400)), 2)
    print("Teie maksavaba tulu on" , raha , "eurot")
    
elif palk > 25200:
    print("Teie maksavaba talu on 0 euro")
    
else:
    print("Ei sobi")