import math
a = int(input("Sisesta liini pikkus:"))
b = int(input("Sisesta postide maksimaalne vahe kaugus:"))
vastus=(a/b)+1
print("Poste on:", +math.ceil((vastus)))

