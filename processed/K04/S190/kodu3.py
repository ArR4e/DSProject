import turtle

piip = turtle.Turtle()
piip.shape('turtle')

def hulknurk(a,b):
    for i in range(a):
        piip.forward(b)
        piip.right(180-(((a-2)*180)/a))



a = int(input("Sisesta hulknurga külgede arv: "))
b = int(input("Sisesta hulknurga ühe külje pikkus: "))

hulknurk(a,b)