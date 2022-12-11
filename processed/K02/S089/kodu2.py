#elektriliin
import math
liinipikkus = int(input('Sisestage liini pikkus: '))
maksimaalkaugus = int(input('Sisestage postide vaheline maksimaalkaugus: '))
if maksimaalkaugus > liinipikkus:
    postiarv = 2
else:
    postiarv = (liinipikkus/maksimaalkaugus + 1)
print(math.ceil(postiarv))
