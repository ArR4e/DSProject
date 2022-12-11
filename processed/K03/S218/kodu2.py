from pykkar import*
create_world("""
########
#  >   #
#      #
#      #
#      #
#      #
########
""")

nurkade_arv = 4
while is_wall() == False and nurkade_arv > 0:
    step()
    
    if is_wall() == True:
        paint()
        nurkade_arv = nurkade_arv -1
    
    while is_wall():
        right()
        
exitonclick()