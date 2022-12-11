from pykkar import *

create_world("""
##########
#<       #
#        #
#        #
#        #
#        #
##########
""")

#nurka jõudmine sõltumata positsioonist ja asukohast
while not is_wall():
    step()
right()
while not is_wall():
    step()

#ristküliku nurkade värvimine
paint()
right()
while not is_wall():
    step()
paint()
right()
while not is_wall():
    step()
paint()
right()
while not is_wall():
    step()
paint()
right()

exitonclick()
    
