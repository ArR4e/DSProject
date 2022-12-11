from math import ceil
a = int(input("Palun sisestage elektriliini pikkus meetrites (täisarvuna) "))
b = int(input("Palun sisestage maksimaalne elektriliini postide vaheline kaugus meetrites (täisarvuna) "))
'''
if a % b == 0:
    print(f"Elektriliini jaoks on vaja: {int(a / b + 1)} posti")
else:
    print(f"Elektriliini jaoks on vaja: {int(a / b + 2)} posti")
'''
print(f"Elektriliini jaoks on vaja: {ceil(a / b)+1} posti")