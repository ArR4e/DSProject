from pykkar import *

create_world("""
###########
#         #
#     ^   #
#         #
#         #
#         #
###########
""")

def liigu():
    if is_wall() == True:
        right()
        paint()
        liigu()
            
    elif is_wall() == False:
        step()
        liigu()
if is_wall() == True:
    right()
    liigu()
while not is_wall():
        step()
        if is_wall() == True:
            right()
            liigu()
