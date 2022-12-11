from pykkar import *
create_world("""
########
#      #
#      #
#      #
#      #
#<     #
########
""")
right()
paint()
while not is_wall():
    step()
paint()
while is_wall():
    right()
while not is_wall():
    step()
paint()
while is_wall():
    right()
while not is_wall():
    step()
paint()
while is_wall():
    right()
    


        

