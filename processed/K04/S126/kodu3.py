import turtle
t = turtle.Turtle()
x = int(input("Külgede arv: "))
y = int(input("Küljepikkus: "))

for n in range(x):
    turtle.forward(y)
    turtle.left(360 / x)
 