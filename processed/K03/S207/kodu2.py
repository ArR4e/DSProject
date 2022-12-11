from pykkar import *
create_world("""
###########
#         #
#         #
#         #
#         #
#   ^     #
#         #
########### """)

while True:
    if is_wall() == True:
        break
    else:
        step()
#kõnnib esimese seinani
right()

n = 0
while n<4:
    if is_wall() == True:
        paint()
        right()
        n +=1
    else:
        step()
        
#kõnnib äärt mööda kuni nurgani, siis värvib, pöörab ja paneb kirja värvutitud nurkade arvu