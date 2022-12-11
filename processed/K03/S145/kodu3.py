arv = abs(int(input("Sisestage arv: ")))
x = 0
y = 0
for i in range(arv+1):
    x = x + i ** 2
    y = y + i
print(y ** 2 - x)
    
    