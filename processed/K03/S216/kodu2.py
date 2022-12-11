from pykkar import *
create_world("""
########
#      #
#      #
#      #
#  <   #
#      #
########
""")
def vasaknurk(): #eeldan et ta vaatab põhja
    while not is_wall():
        step()
    right()
    right()
    right()
    while not is_wall():
        step()

if get_direction() == N:
    vasaknurk()
    paint()
elif get_direction() == E:
    right()
    right()
    right()
    vasaknurk()
    paint()
elif get_direction() == S:
    right()
    right()
    vasaknurk()
    paint()
else:
    right()
    vasaknurk()
    paint()
right()
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
