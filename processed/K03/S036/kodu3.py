#ruudud

n = int(input("Sisestage naturaalarv:"))
def arvud(n):
    lst1 =[]
    lst2 = []
    for i in range(n+1):
        lst1 += [i**2]
        lst2 += [i]
    esimene = sum(lst1)
    teine = (sum(lst2))**2
    print(teine - esimene)

arvud(n)