from pykkar import *
create_world("""
########
#      #
#>     #
#      #
#      #
#      #
########
""")

while is_wall() == False:
    step()
    a=0
    b=4
right()
while a<b:
    if is_wall() == True:
        paint()
        right()
        a+=1
    else:
        step()
exitonclick()