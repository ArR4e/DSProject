from pykkar import *

create_world("""
###########
#  >      #
#         #
#         #
#         #
#         #
###########
""")

while True:

    #lähme nurk
    while not is_wall(): 
        step()

    right()    

    while not is_wall(): 
        step()

    #küsime kas nurk on värvitud
    värvitud = is_painted()
    if  värvitud == False:
        
        paint() #kui ei ole siis värvime
    else:
        break








