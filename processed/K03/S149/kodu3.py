n = int(input("Siesesta naturaalarv: "))
ruut_sum = 0
for x in range(n):
    ruut_sum += (x + 1) ** 2
print(round(((1 + n) / 2 * 10) ** 2 - ruut_sum))