import math

liini_pikkus = int(input("Sisestage liini pikkus meetrites: "))
postide_vaheline_kaugus = int(input("Sisestage postide vaheline maksimaal kaugus meetrites: "))

postide_arv = math.ceil(liini_pikkus / postide_vaheline_kaugus)

print(postide_arv + 1)
