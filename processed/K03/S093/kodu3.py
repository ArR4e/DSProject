arv = float(input("Sisestage oma astme: "))
vastus_1 = float((1 ** arv + 2 ** arv + 3 ** arv + 4 ** arv + 5 ** arv \
                + 6 ** arv + 7 ** arv + 8 ** arv + 9 ** arv + 10 ** arv))
vastus_2 = float(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10) ** arv
print(int(vastus_2 - vastus_1))