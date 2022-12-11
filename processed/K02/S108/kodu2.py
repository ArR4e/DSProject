from math import ceil
k=int(input("sisesta postide vaheline kaugus "))
p=int(input("sisesta liini pikkus "))
if k>40:
    print("maks kaugus on 40")
    exit()
else:    
    arv = (p/k)+1

print(int(arv))