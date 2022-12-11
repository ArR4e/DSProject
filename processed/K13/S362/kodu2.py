from turtle import*
speed(0)
def fraktaal(mitmes_tase,pikkus):
    
  

#     for suvalinenr in range(3):
    i=3
    while i >0:
        forward(pikkus)
        if mitmes_tase>1:
            pikkus=pikkus*0.5
            left(90)
            fraktaal(mitmes_tase-1, pikkus)
            right(90)
            pikkus=pikkus/0.5
            
        right(90)
        i=i-1
    forward(pikkus)
    right(90)
       
fraktaal(4,100)       
exitonclick()            
       