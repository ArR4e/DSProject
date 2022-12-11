from pykkar import *

create_world("""
##########
#     <  #
#        #
#        #
#        #
#        #
##########
""")

right()
right()

sammud = 8
while sammud > 0:
    if is_wall():
        break
    else:
        step()
        sammud -= 1
paint()
right()

sammud = 8
while sammud > 0:
    if is_wall():
        break
    else:
        step()
        sammud -= 1
paint()
right()

sammud = 8
while sammud > 0:
    if is_wall():
        break
    else:
        step()
        sammud -= 1
paint()
right()

sammud = 8
while sammud > 0:
    if is_wall():
        break
    else:
        step()
        sammud -= 1
paint()
right()

exitonclick()