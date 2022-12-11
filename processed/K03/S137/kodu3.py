import math 
ruut1 = ruut2 = arv = i = 0
n = int(input("Sisesta naturaalarv n: "))
while n >= i:
    ruut1 = i**2 + ruut1
    arv = i + arv
    i += 1
ruut2 = arv**2
print (ruut1)
print(ruut2)
vastus = ruut2 - ruut1
print("vahe on", vastus)
