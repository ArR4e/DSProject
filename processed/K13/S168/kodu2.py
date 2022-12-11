from turtle import*

def fractal(length, depth):
    speed(8)
    if depth == 1:
        fd(length)
        left(90)
        fd(length)
        left(90)
        fd(length)
        left(90)
        fd(length)
    else:  
        fd(length)
        fractal(length * 0.4, depth - 1)
        fd(length)
        fractal(length * 0.4, depth - 1)
        fd(length)
        fractal(length * 0.4, depth - 1)
        fd(length)
    
  
    
exitonclick()