from pykkar import *

create_world("""
#################
#               #
#               #
#               #
#  >            #
#################
""")
suund = get_direction()
if suund == 'N':
    right()
    right()
    right()
if suund == 'E':
    right()
    right()
if suund == 'S':
    right()
suund = get_direction()
if suund == 'W':
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