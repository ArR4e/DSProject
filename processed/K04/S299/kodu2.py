def summa(x,y):
    c=299792.458
    return (x+y)/(1+(x*y/c**2))

a=float(input('Sisestage kiirus1: '))
b=float(input('Sisestage kiirus2: '))
d=float(input('Sisestage kiirus3: '))
e=float(input('Sisestage kiirus4: '))

absumma= summa(a,b)
abcsumma= summa(absumma,d)
lõppsumma= summa(abcsumma,e)
print('Kiiruste summa on',lõppsumma,'km/h')