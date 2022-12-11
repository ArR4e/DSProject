from pykkar import*

create_world("""
#########
#       #
#       #
#       #
#       #
#   <   #
#########""")

suund = get_direction()
while not (suund=="N"):
    right()
    suund = get_direction()
sein=is_wall()
while sein==False:
    step()
    sein=is_wall()
right()
sein=False
while sein==False:
    step()
    sein=is_wall()
right()
paint()
a=0
while a<3:
    sein=False
    while sein==False:
        step()
        sein=is_wall()
    right()
    paint()
    a+=1
exitonclick()