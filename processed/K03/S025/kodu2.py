from pykkar import *

create_world('''
#####
#  v#
#   #
#   #
#   #
#####''')

while not is_wall():
    step()
while is_wall():
    right()
    while not is_wall():
        step()
    if is_painted():
        break
    elif is_wall():
        paint()
    else:
        continue