import turtle as trt

a = trt.Turtle()
s = trt.Screen()
a.speed(0)

def fractal(turtle, depth, dist, dir):
    for i in range(3):
        a.forward(dist)

        if depth >= 1:
            fractal(turtle, depth - 1,  dist / 2, -dir)

        turtle.right(dir)

    turtle.forward(dist)
    turtle.right(dir)

fractal(a, 2, 100, 90)

s.exitonclick()