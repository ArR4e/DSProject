import math

a = int(input("Kui pikka liini soovid ehitada (täisarv): "))
b = int(input("Kui suured vahed on postidel maksimaalselt(täisarv): "))

c = (a/b)+1
c = math.ceil(c)
c = str(c)
print("Miinimum postide arv on "+c)

