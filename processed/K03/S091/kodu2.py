from pykkar import*

create_world("""
##############
#            #
#            #
#     >      #
#            #
#            #
#            #
#            #
##############
""")

pööramisi = 0

while not is_wall() == True:
    step()
    if is_wall() == True and pööramisi == 0:
        right()
        pööramisi += 1
    else:
        if is_wall() == True and pööramisi == 1:
            paint()
            right()
            
exitonclick()