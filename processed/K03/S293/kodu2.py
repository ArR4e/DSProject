from pykkar import*
create_world("""
########
#      #
#      #
#      #
# <    #
#      #
########
""")
värvitudnurki=1
while not is_wall():
    step()
    if is_wall():
        right()
        break
while värvitudnurki <= 4:
    step()
    
    if is_wall():
        right()
        paint()
        värvitudnurki +=1

exitonclick()