from pykkar import *
create_world('''
########
#      #
#      #
#      #
#  <   #
########
''')
sammud = 4
while not is_wall ():
    step()
else:
    right()
while sammud > 0:
    while not is_wall ():
        step()
    else:
        paint()
        right()
    sammud -= 1