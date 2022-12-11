from pykkar import *

create_world("""
#########
#       #
#       #
#  ^    #
#       #
#       #
#       #
#########
""")

a=0


while is_wall() == False:
    step()
while is_wall() == True:
    right()
while is_wall() == False:
    step()
while is_wall() == True:
    paint()
    right()
while a<3:
    while is_wall() == False:
        step()
    while is_wall() == True:
        paint()
        right()
    a+=1
exitonclick()