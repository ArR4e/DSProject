from pykkar import *
create_world("""
##########
#        #
#        #
#        #
#    >   #
#        #
##########
""")
i=0
while not is_wall():
    step()
    if is_wall():
        break
    else:
        step()
right()
while not is_wall():
    step()
    if is_wall():
        paint()
        i+=1
        right()
        if i==4:
            break