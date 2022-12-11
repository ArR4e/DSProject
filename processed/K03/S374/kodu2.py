from pykkar import *

create_world('''
################
#              #
#              #
#              #
#              #
#              #
#    <         #
#              #
################
''')

nurgad=4

while not is_wall():
    step()
    
right()
    
while nurgad != 0:
    while not is_wall():
        step()
    paint()
    right()
    nurgad-=1