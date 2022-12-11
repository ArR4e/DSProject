from pykkar import *
create_world("""
#######
#  >  #
#     #
#     #
#######
""")

while not is_wall(): 
    step()
    step()
    paint()
    right()
    step()
    step()
    paint()
    right()
    step()
    step()