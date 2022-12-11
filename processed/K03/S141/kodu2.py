from pykkar import *

create_world("""
###########
#         #
#    v    #
#         #
#         #
#         #
###########
""")

if is_wall():
    right()
    while not is_wall():
        step()
        if is_wall():
            paint()
else:
    while not is_wall():
        step()
        if is_wall():
            right()
            while not is_wall():
                step()
                if is_wall():
                    paint()

right()
while not is_wall():
    step()
    if is_wall():
            paint()
right()
while not is_wall():
    step()
    if is_wall():
            paint()
right()
while not is_wall():
    step()
    if is_wall():
            paint()
