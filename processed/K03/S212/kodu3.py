n = int(input("Sisestage naturaalarv: "))
total = 0
squareTotal = 0
while n > 0:
    total += n
    squareTotal += n**2
    n -= 1
answer = abs(total**2-squareTotal)
print(answer)