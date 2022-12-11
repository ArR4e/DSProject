aastane_tulu = float(input("Sisestage aastane tulu: "))
if aastane_tulu < 6000:
    print("Maksuvaba tulu on", str(round(aastane_tulu, 2))+"€ aastas.")
elif 6000 <= aastane_tulu < 14400:
    print("Maksuvaba tulu on 6000.00€ aastas.")
elif 14400 <= aastane_tulu < 25200:
    print("Maksuvaba tulu on", str(round(6000-6000/10800*(aastane_tulu-14400),2))+"€ aastas.")
else:
    print("Maksuvaba tulu on 0.00€")
