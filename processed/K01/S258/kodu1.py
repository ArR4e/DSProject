from turtle import *

#puuduv paadi ots
left(180)
forward(5)
left(180)
forward(5)

#paadi kere
forward(100)

#paadi kabiin)
left(90)
forward(30)
right(90)
forward(50)
right(90)
forward(30)
left(90)

#paadi kere2
forward(50)
right(90)
#paadi taguots kaarega
forward(20)
x=0
while x!=90:
    right(1)
    forward(1)
    x+=1

#paadi alusotsa kaarega
forward(40)
x=0
while x!=72:
    right(1)
    forward(2)
    x+=1

#laineteks valmistumine
right(18)
left(90)
up()
forward(500)
left(90)
forward(20)
left(90)
down()


#lained
n=0

while n!=5:
    x=0
    while x!=30:
        right(1)
        forward(2)
        x+=1
    x=0
    while x!=60:
        left(1)
        forward(2)
        x+=1
    x=0
    while x!=30:
        right(1)
        forward(2)
        x+=1
    n+=1

print("Valmis.")
exitonclick()