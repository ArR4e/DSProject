from math import ceil
liini_pikkus= int(input('sisesta liini kogu pikkus: '))
postivahe= int(input('sisesta postide maksimaalkaugus: '))

postide_arv= ceil(liini_pikkus/postivahe)

if postide_arv < 2 :
    postide_arv = postide_arv + 1
elif liini_pikkus == postivahe:
    postide_arv= 2
elif liini_pikkus <= postivahe:
    postide_arv= postide_arv+1
else:
    postide_arv= postide_arv +1



print(liini_pikkus,'meetrise liini jaoks on vaja vähemalt'
      ,postide_arv,'posti.')

