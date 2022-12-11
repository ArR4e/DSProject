#Kodutöö 4-2

c = 299792458
def summa(u, v):
    return((u+v)/(1+((u*v)/(c**2))))
one = float(input("1 = "))
two = float(input("2 = "))
three = float(input("3 = "))
four = float(input("4 = "))
print(summa(one, summa(two, (summa(three, four)))))