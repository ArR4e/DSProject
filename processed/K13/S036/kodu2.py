from turtle import *
def ruut(n,w):
    if n>=1:
        fd(w)
        lt(90)
        i=1
        while i<=2:
            ruut(n-1,w*0.5)
            lt(180)
            fd(w)
            lt(90)
            i +=1
        ruut(n-1,w*0.5)
        lt(180)
        fd(w)
        rt(90)
        
       
        
    

speed(0)
ruut(3,100)

exitonclick()