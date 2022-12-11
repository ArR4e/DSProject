from math import ceil
from math import floor
a = float(input("Missugune on sinu soovitud liini pikkus? Täisarv meetrites "))
b = float(input("Palju on sinu soovitud maksimaalne postide kaugus üksteisest? Täisarv meetrites "))
c = a/b + 1
if a > 0 and a < 5000 and b > 0 and b <= 50 and abs((a/b) - floor(a/b)) < 1:
    print(("Minimaalselt ehituseks vaja minev postide arv on ")) and print(ceil(c))     
else:
    print("Ebasobivad andmed")
