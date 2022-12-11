import math
x = int(input('Sisesta liini pikkus meetrites täisarvuna:'))
y = int(input('Sisesta postide maksimaalsed vahed meetrites täisarvuna:'))
if x == y:
    print('Vaja läheb', 2, 'posti')
if x > y:
    z = math.ceil((x/y) + 1)
    print('Vaja läheb', z, 'posti')
else:
    print('Vaja läheb 2 posti')