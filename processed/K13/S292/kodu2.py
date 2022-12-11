import turtle as t

t.speed(0)
 
def ruut(kylg, sygavus):
    if sygavus == 0:
        return
    t.forward(kylg)
    t.left(90)
    ruut(kylg/2, sygavus-1)
    t.right(180)
    t.forward(kylg)
    t.left(90)
    ruut(kylg/2, sygavus-1)
    t.right(180)
    t.forward(kylg)
    t.left(90)
    ruut(kylg/2, sygavus-1)
    t.right(180)
    t.forward(kylg)
    t.right(90)
  

ruut(100,4)

t.exitonclick()