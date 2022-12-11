# 1. Maksuvaba tulu
# Maksuvaba tulu määr sõltub aastatulust:

# aastatuluga kuni 6000 eurot on maksuvaba tulu võrdne aastatuluga
# aastatuluga 6000 kuni 14 400 eurot on maksuvaba tulu 6000 eurot aastas
# aastatuluga 14 400 kuni 25 200 eurot arvutatakse maksuvaba tulu vastavalt valemile 6000 – 6000 ÷ 10 800 × (aastatulu – 14 400)
# aastatuluga üle 25 200 euro on maksuvaba tulu 0 eurot.
# Kirjuta programm, mis küsib kasutaja aastatulu (mittenegatiivne ujukomaarv) ja arvutab ning
# väljastab ekraanile maksuvaba tulu ümardatuna kahe kohani pärast koma.

# Näide
#  Sisesta aastatulu: 16825
#  Maksuvaba tulu on 4652.78 eurot.

tulu = float(input("Sisesta aastatulu: "))

if tulu < 6000:
    print("Maksuvaba tulu on", round(tulu,2), "eurot.")
elif 6000 <= tulu < 14400:
    print("Maksuvaba tulu on 6000 eurot.")
elif 14400 <= tulu < 25200:
    maksuvaba = 6000 - 6000 / 10800 * (tulu - 14400)
    print("Maksuvaba tulu on", round(maksuvaba,2),  "eurot.")
else:
    print("Maksuvaba tulu on 0 eurot.")