import turtle
x = int(input("Sisesta külgede arv: "))
y = int(input("Sisesta külgede pikkus: "))
def funktsioon(x, y):
    return(turtle.Turtle())
for n in range(x):
    turtle.forward(y)
    turtle.right(360 / x)