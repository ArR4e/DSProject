n = int(input('Sisesta naturaalarv: '))

i = 1
sqrsum = 0
while i <= n:
    sqrsum += i ** 2
    i += 1

i = 1
sumsqr = 0
while i <= n:
    sumsqr += i
    i += 1
sumsqr = sumsqr ** 2

print(sumsqr - sqrsum)