import turtle
import random
    
def hn_joon(k_arv, k_pikk):
    i = 0
    k_arv = random.randint(3, 10)
    k_pikk = random.randint(10, 100)
    while i < k_arv:
        turtle.forward(k_pikk)
        turtle.right(360/k_arv)     
        i += 1
        
            
k_arv = random.randint(3, 10)
k_pikk = random.randint(10, 100)
hn_arv = 0
while hn_arv < 30:
    hn_joon (k_arv, k_pikk)
    hn_arv += 1
    turtle.up()
    turtle.goto(random.randint(-300,300), random.randint(-300,300))
    turtle.down()
turtle.exitonclick()
