from pykkar import *

create_world('''
########
#      #
#      #
#   <  #
#      #
#      #
########
''')
j=1
while j < 3:
    while not is_wall():
        step()
    right()
    j += 1

i = 1
while i < 5:
    while not is_wall():
        step()
    paint()
    right()
    i += 1