import os

teepikkus=float(input('Sisesta tee pikkus kilomeetrites: '))

fail ='taksohinnad.txt'
f = open(fail)

def hind(istumine,kmh,km):
    hind=kmh*km+istumine
    return hind

taksode_hinnad=[]
nimed=[]

for rida in f:
    a=list(rida)
    b=''.join(a).split(',')
    b[-1]=b[-1].strip()
    nimi=b[0]
    takso_hind=hind(float(b[1]),float(b[2]),teepikkus)
    taksode_hinnad.append(takso_hind)
    nimed.append(nimi)
    
filesize = os.path.getsize(fail)

if filesize==0:
    print('Taksohindu ei leidtud.')
else:
    väikseim = min(taksode_hinnad)
    i = taksode_hinnad.index(väikseim)
    print('Odavaim takso on', nimed[i])

f.close() 


                