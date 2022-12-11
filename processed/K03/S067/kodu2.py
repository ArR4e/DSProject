from pykkar import *

create_world('''
##########
#        #
#    <   #
#        #
#        #
#        #
#        #
#        #
##########
''')
while is_wall() is False:
    step()
if is_wall() is True:
    right()
    while is_wall() is False:
        step()
    else:
        paint()
        right()
i = 0
while i < 3:
    while is_wall() is False:
        step()
    if is_wall() is True:
        right()
        paint()
        i += 1
