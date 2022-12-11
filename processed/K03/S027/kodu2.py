from pykkar import *
create_world('''
###########
#         #
#         #
#         #
#         #
#         #
#     <   #
#         #
#         #
###########
''')
while True:
    if is_wall():
        right()
    else:
        step()
    if is_wall():
        right()
        while is_wall() == False:
                step()
                if is_wall():
                    if is_painted():
                        break
                    else:
                        paint()
                        right()
                        step()
    if is_painted():
        break