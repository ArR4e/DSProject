from pykkar import *

create_world("""
############
#          #
#     >    #
#          #
#          #
############
""")

#Defineerin funktsiooni, mis käivitatakse, kui pykkar kõnnib vastu seina
#Funktsiooni point on see, et kui pykkar on vastu seina kõndinud pöörab ta kolm korda ja kui ühel nendest kolmest pöördest on sein vastas teame, et oleme nurgas ja värvime.

def nurk():
    pöörete_arv = 0
    while pöörete_arv <= 2:
        right()
        if is_wall():
            paint()
        pöörete_arv += 1
        
while not is_wall():
    step()
    if is_wall():
        nurk()
    
    

