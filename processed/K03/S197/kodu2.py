from pykkar import *
painted = 0

create_world('''
#########
#       #
# >     #
#       #
#       #
#       #
#########
''')

while True:
    if is_wall():
        if painted == 4:
            break
        right()
        while painted < 4:
            if is_wall():
                paint()
                right()
                painted += 1
            else:
                step()
    else:
        if painted == 4:
            break
        step()