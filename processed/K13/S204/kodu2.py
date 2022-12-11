from turtle import*


def fraktal(t, k):
    if t > 0:
    
        forward(k)
        
        if not t == 1:
            right(90)
            fraktal(t-1, 0.5*k)
            right(90)
            forward(k)
            right(90)
            fraktal(t-1, 0.5*k)
            right(90)
            forward(k)
            right(90)
            fraktal(t-1, 0.5*k)
            right(90)
            forward(k)
            
            
        else:
            left(90)
            forward(k)
            left(90)
            forward(k)
            left(90)
            forward(k)
            
             
        
       

print(fraktal(3, 100))


exitonclick()
            
            