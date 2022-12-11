a_tulu = float(input("Sisesta aastatulu: ")) #sisend: aastatulu
while a_tulu <= 0:
    a_tulu = float(input("Sisesta aastatulu (peab olema mittenegatiivne arv): ")) #sisesta positiivne arv

m_tulu = 0.0 #maksuvaba tulu
määr_1 = float(6000)
määr_2 = float(14400)
määr_3 = float(25200)

if a_tulu < määr_1: #kui aastatulu < 6000
    m_tulu = a_tulu
elif a_tulu < määr_2: #kui 6000 <= aastatulu < 14400
    m_tulu = määr_1
elif a_tulu < määr_3: #kui 14400 <= aastatulu < 25200
    m_tulu = määr_1-määr_1/10800*(a_tulu-määr_2)
print("Maksuvaba tulu:", round(m_tulu, 2)) #kui aastatulu >= 25200, siis esialgne väärtus 0.0