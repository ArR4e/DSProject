import turtle
pen = turtle.Turtle()
n = int(input("Sisesta külgede arv: "))
b = float(input("Sisesta külje pikkus: "))
        
def figure(n,b):
    for i in range(n):
        pen.forward(b)
        pen.left(360/n)
        
for i in range(30):
    figure(i,b)
    
exitonclick()