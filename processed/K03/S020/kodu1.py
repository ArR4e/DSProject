'''
Maksuvaba tulu määr sõltub aastatulust:

aastatuluga kuni 6000 eurot on maksuvaba tulu võrdne aastatuluga
aastatuluga 6000 kuni 14 400 eurot on maksuvaba tulu 6000 eurot aastas
aastatuluga 14 400 kuni 25 200 eurot arvutatakse maksuvaba tulu vastavalt valemile
6000 – 6000 ÷ 10 800 × (aastatulu – 14 400)
aastatuluga üle 25 200 euro on maksuvaba tulu 0 eurot.
Kirjuta programm, mis küsib kasutaja aastatulu (mittenegatiivne ujukomaarv)
ja arvutab ning väljastab ekraanile maksuvaba tulu ümardatuna kahe kohani pärast koma.

'''

aastatulu=float(input("Sisesta aastatulu:"))
maksuvaba_tulu = float(0)

if aastatulu <= 6000:
    maksuvaba_tulu=aastatulu
elif aastatulu > 6000 and aastatulu <= 14400:
    maksuvaba_tulu = 6000
elif aastatulu > 14400 and aastatulu <= 25200:
    maksuvaba_tulu=6000-6000/10800*(aastatulu-14400)
elif aastatulu > 25200:
    maksuvaba_tulu=0
print(round(maksuvaba_tulu,2))
