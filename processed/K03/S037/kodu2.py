from pykkar import *

create_world("""
#############################
#             >             #
#                           #
#                           #
#                           #
#                           #
#############################
""")

nurki = 1

while nurki <= 4:
    while not is_wall():
        step()
    paint()
    right()
    nurki += 1
    
    
right()
right()