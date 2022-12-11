from pykkar import *

create_world("""

############
#        v #
#          #
#          #
############

""")


while True:
    step()
    if is_wall():
        try:
            right()
            step()
            break
        except:
            right()
            break
            right()
while True:
    step()
    if is_wall():
        right()
        paint()
        
exitonclick()