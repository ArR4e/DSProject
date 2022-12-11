a = int(input("Liini pikkus: "))
b = int(input("Postide maksimaalkaugus: "))

c = a//b
print(c)
print("Postide arv: ", end="")

if a == b or c < 1:
    print(2)
elif a - b * c == 0:
    print(c+1)
else:
    print(c+2)    
    
