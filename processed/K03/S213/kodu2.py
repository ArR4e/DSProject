from pykkar import *
create_world("""
########
#      #
#      #
#  v   #
#      #
#      #
########
""")

i = 0
while i < 4:
    if not is_wall():
        step()
    else:
        right()
        if not is_wall():
            right()
            if not is_wall():
                right()
                if is_wall():
                    i+=1
                    paint()
                    if i < 4:
                        right()
                        right()
                        step()