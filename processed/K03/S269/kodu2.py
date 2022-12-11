from pykkar import *

create_world("""
########
#     ^#
#      #
#      #
#      #
#      #
########
""")


a = 0

while a == 0:
    if is_wall():
        right()
        a = 1
    else:
        step()
        
count = 0
while count < 4:
    if is_wall():
        paint()
        right()
        count += 1
    else:
        step()
    