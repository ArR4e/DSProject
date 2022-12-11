#elektripostide ülesanne
l = int(input('Sisesta liini pikkus meetrites: '))
post_l = int(input('Sisesta postide maksimaalkaugus üksteisest: '))

import math
x = l / post_l
vahede_arv = math.ceil(x)
vaja_post = str(vahede_arv + 1)
             
print('Ehitamiseks on minimaalselt vaja: ' + vaja_post + ' posti')
             
        
           