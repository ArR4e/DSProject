from turtle import *
r=int(input("sisesta arv 1-20: "))

up()
left(180)
forward(15*r)
left(90)
forward(10*r)
left(90)
down()

#joonistab paadi
color("red")
begin_fill()
forward(30*r)
right(120)
forward(10*r)
right(60)
forward(20*r)
right(60)
forward(10*r)
end_fill()

#liigub akende asukohta
up()
right(120)
forward(3*r)
right(90)
forward(4*r)
left(90)
down()

#joonistab akna

pensize(int(r/2))
i=1
up()
while i<6:
    pencolor("blue")
    begin_fill()
    fillcolor("white")
    forward(4*r)
    down()
    circle(r)
    end_fill()
    up()
    i+=1

#liigub masti asukohta
pencolor("black")
pensize(2)
up()    
left(180)
forward(8*r+r/5)
right(90)
forward(4*r)

#joonistab masti
down()
forward(30*r)
right(90)
forward(2*r/5)
right(90)
forward(30*r)

#liigub lipu asukohta
up()
pensize(1)
right(180)
forward(29*r)

#joonistab lipu
color("red")
begin_fill()
down()
right(105)
forward(3*r)
right(150)
forward(3*r)
end_fill()
left(75)
forward(r)


#joonistab purje
pencolor("blue")
left(30)
forward(25*r)
right(120)
forward(20*r+2*r/5)
right(120)
forward(15*r)
up()

exitonclick()
