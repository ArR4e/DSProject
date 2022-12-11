nurk = int(input("Mitu nurka? "))
pikkus = int(input("Mis on küljepikkus? "))
from turtle import *
külg = nurk + 1
for _ in range (külg):
    forward(pikkus)
    left(360/nurk)


exitonclick()