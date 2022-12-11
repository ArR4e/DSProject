#aastatuluga kuni 6000 eurot on maksuvaba tulu võrdne aastatuluga
#aastatuluga 6000 kuni 14 400 eurot on maksuvaba tulu 6000 eurot aastas
#aastatuluga 14 400 kuni 25 200 eurot arvutatakse maksuvaba tulu vastavalt valemile 6000 – 6000 ÷ 10 800 × (aastatulu – 14 400)
#aastatuluga üle 25 200 euro on maksuvaba tulu 0 eurot.

aastatulu = float(input("Tere! Palun sisesta teie aastatulu ja vajuta ENTER: "))
if aastatulu <= 6000:
    print("Teie maksuvaba tulu", aastatulu)
else:
    if aastatulu > 6000 and aastatulu <= 14400:
        print("Teie maksuvaba tulu on 6000 eurot aastas.")
    else:
        if aastatulu >= 14400 and aastatulu <= 25200:
            b = round(6000 - (6000 / 10800) * (aastatulu - 14400), 2)
            print("Teil on vaja maksta ",b)
        else:
            print("Teie maksuvaba tulu on 0 eurot aastas.")
