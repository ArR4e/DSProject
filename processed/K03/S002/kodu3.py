n = int(input("Arv: "))
n1 = 0
n2 = 0
for i in range(1,n+1):
    n1 += i**2
    n2 += i
print(n2**2-n1)