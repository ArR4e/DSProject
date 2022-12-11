#Alustab korduse kuni saab sisestuseks mittenegatiivse ujukomaarvu
while True:
    try:
        aastatulu = float(input("Sisesta aastatulu: "))
        if aastatulu >= 0:
            break
        print("Arv peab olema positiivne.")
    except:
        print("Midagi läks valesti.")

#Kontrollib kui suur on aastatulu ja arvutab selle järgi maksuvaba tulu
if aastatulu < 6000:
    maksuvaba = aastatulu
elif 6000 <= aastatulu < 14400:
    maksuvaba = 6000.0
elif 14400 <= aastatulu <= 25200:
    maksuvaba = 6000 - 6000 / 10800 * (aastatulu - 14400)
else:
    maksuvaba = 0

#Prindib saadud tulemuse ümardades 2 koma kohaga
print(f"Maksuvaba tulu on {round(maksuvaba, 2)} eurot.")