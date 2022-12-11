from pykkar import *

create_world("""
########
#      #
#      #
#      #
#   <  #
#      #
########
""")

suund = get_direction()


if suund == 'W':
    right()
    
elif suund == 'S':
    right()
    right()
    
elif suund == 'E':
    right()
    right()
    right()

while not is_wall():
    step()
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

while not is_wall():
    step()
paint()
right()



