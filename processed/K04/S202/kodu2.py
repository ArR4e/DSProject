from math import*
c = 299792.458

s1 = float(input("Sisesta esimese keha kiirus: "))
s2 = float(input("Sisesta teise keha kiirus: "))
s3 = float(input("Sisesta kolmanda keha kiirus: "))
s4 = float(input("Sisesta neljanda keha kiirus: "))

def summa(x, y):
    A = (x + y) / (1 + ((x*y) / c**2))
    return A

S1 = summa(s1, s2)
S2 = summa(S1, s3)
S3 = summa(S2, s4)

print(S3)