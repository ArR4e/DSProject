from pykkar import *
create_world("""
#######
#     #
#  N  #
#     #
#######
""")
while is_wall()==False:
    step()
right()
while is_wall()==False:
    step()
paint()
right()
while is_wall()==False:
    step()
paint()
right()
while is_wall()==False:
    step()
paint()
right()
while is_wall()==False:
    step()
paint()


 